# Vista_Escaleras.py
import sys
import time as t
from PyQt5 import uic, QtWidgets, QtCore
import Vista_Grafica

qtCreatorFile = "Vista_Escaleras.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Referencia a la ventana principal
        self.parent = parent

        # Área de los Signals
        self.btn_Mostrar.clicked.connect(self.activar_mostrar_datos)
        self.btn_Prender.clicked.connect(self.prender_apagar)
        self.btn_Visualizar.clicked.connect(self.visualizar_grafica)

        # Datos del sensor y estado
        self.pir_datos = [0, 0]  # Dos sensores PIR
        self.estado = 0  # 0: apagado, 1: encendido

        # Historial de mediciones para la gráfica
        self.historial = []
        self.max_historial = 20

        # Ventana de gráfica
        self.ventana_grafica = None

        # Flag para indicar si se deben mostrar los datos
        self.mostrar_datos_activo = False

        # Temporizador para actualizar la interfaz
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_datos)
        self.timer.start(500)  # Actualizar cada 500 ms

    def actualizar_datos(self):
        # Actualizar datos del sensor
        if self.parent and hasattr(self.parent, 'pir_datos'):
            # Si hay referencia a la ventana principal, obtener datos de ahí
            self.pir_datos = self.parent.pir_datos.copy()
            self.estado = self.parent.escaleras_estado
            if hasattr(self.parent, 'historial_escaleras'):
                self.historial = self.parent.historial_escaleras.copy()
        else:
            # En caso contrario, simular localmente
            import random
            self.pir_datos[0] = random.randint(0, 1)
            self.pir_datos[1] = random.randint(0, 1)
            self.estado = 1 if (self.pir_datos[0] == 1 or self.pir_datos[1] == 1) else 0

            # Actualizar historial
            self.historial.append(self.estado)
            if len(self.historial) > self.max_historial:
                self.historial.pop(0)

        # Actualizar interfaz si está activado
        if self.mostrar_datos_activo:
            self.mostrar_datos()

        # Si la ventana de gráfica está abierta, actualizar sus datos
        if self.ventana_grafica:
            self.ventana_grafica.actualizar_datos(self.historial.copy())

    def activar_mostrar_datos(self):
        # Cambiar el estado de mostrar datos
        self.mostrar_datos_activo = not self.mostrar_datos_activo

        # Cambiar el texto del botón según el estado
        if self.mostrar_datos_activo:
            self.btn_Mostrar.setText("Detener")
            # Mostrar datos inmediatamente
            self.mostrar_datos()
        else:
            self.btn_Mostrar.setText("Mostrar")

    def mostrar_datos(self):
        self.listWidget.clear()

        # Agregar información al listWidget
        self.listWidget.addItem(f"Sensor PIR 1: {'Detecta movimiento' if self.pir_datos[0] == 1 else 'Sin movimiento'}")
        self.listWidget.addItem(f"Sensor PIR 2: {'Detecta movimiento' if self.pir_datos[1] == 1 else 'Sin movimiento'}")
        self.listWidget.addItem(f"Estado: {'Encendido' if self.estado else 'Apagado'}")

        # Agregar información de la lógica
        if self.pir_datos[0] == 1 or self.pir_datos[1] == 1:
            self.listWidget.addItem("Se detecta movimiento en al menos un sensor")
        else:
            self.listWidget.addItem("No se detecta movimiento en ningún sensor")

    def prender_apagar(self):
        if self.btn_Prender.text() == "Prender":
            self.estado = 1
            self.btn_Prender.setText("Apagar")
            self.parent.escaleras_estado = 1
            self.parent.escaleras = False
        else:
            self.estado = 0
            self.parent.escaleras_estado = 0
            self.parent.escaleras = True
            self.btn_Prender.setText("Prender")

        # Si está activada la actualización de datos, actualizar ahora
        if self.mostrar_datos_activo:
            self.mostrar_datos()

    def visualizar_grafica(self):
        # Crear la ventana de gráfica si no existe
        if not self.ventana_grafica:
            self.ventana_grafica = Vista_Grafica.MyApp(tipo_sensor="escaleras", datos=self.historial.copy())
        else:
            # Actualizar los datos si ya existe
            self.ventana_grafica.actualizar_datos(self.historial.copy())
            self.ventana_grafica.tipo_sensor = "escaleras"
            self.ventana_grafica.actualizar_titulo()

        # Mostrar la ventana
        self.ventana_grafica.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())