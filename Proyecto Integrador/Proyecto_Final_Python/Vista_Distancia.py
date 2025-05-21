import sys
import time as t
from PyQt5 import uic, QtWidgets, QtCore
import Vista_Grafica

qtCreatorFile = "Vista_Distancia.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Referencia a la ventana principal (puede ser None si se ejecuta independientemente)
        self.parent = parent

        # Área de los Signals
        self.btn_Mostrar.clicked.connect(self.activar_mostrar_datos)
        self.btn_Prender.clicked.connect(self.prender_apagar)
        self.btn_Visualizar.clicked.connect(self.visualizar_grafica)

        # Datos del sensor y estado
        self.distancia = 0  # Valor inicial (50 cm)
        self.VACIO = 15  # Valor cuando está vacío (cm)
        self.LLENO = 0  # Valor cuando está lleno (cm)
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
        if self.parent and hasattr(self.parent, 'distancia_dato'):
            # Si hay referencia a la ventana principal, obtener datos de ahí
            self.distancia = self.parent.distancia_dato
            if hasattr(self.parent, 'historial_distancia'):
                self.historial = self.parent.historial_distancia.copy()
        else:
            # En caso contrario, simular localmente
            self.distancia += QtCore.QRandomGenerator.global_().bounded(-2, 3)
            self.distancia = max(self.LLENO, min(self.VACIO, self.distancia))

            # Actualizar historial
            self.historial.append(self.distancia)
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

        # Calcular el nivel del tinaco en porcentaje
        nivel_porcentaje = 100 * (self.VACIO - self.distancia) / (self.VACIO - self.LLENO)
        nivel_porcentaje = max(0, min(100, nivel_porcentaje))

        # Agregar información al listWidget
        self.listWidget.addItem(f"Distancia actual: {self.distancia:.1f} cm")
        self.listWidget.addItem(f"Nivel del tinaco: {nivel_porcentaje:.1f}%")
        self.listWidget.addItem(f"Estado: {'Encendido' if self.estado else 'Apagado'}")

        # Agregar contexto
        if nivel_porcentaje < 20:
            self.listWidget.addItem("¡Advertencia! Nivel bajo del tinaco")
        elif nivel_porcentaje > 80:
            self.listWidget.addItem("Tinaco casi lleno")

    def prender_apagar(self):
        if self.btn_Prender.text() == "Prender":
            self.estado = 1
            self.btn_Prender.setText("Apagar")
        else:
            self.estado = 0
            self.btn_Prender.setText("Prender")

        # Si está activada la actualización de datos, actualizar ahora
        if self.mostrar_datos_activo:
            self.mostrar_datos()

    def visualizar_grafica(self):
        # Crear la ventana de gráfica si no existe
        if not self.ventana_grafica:
            self.ventana_grafica = Vista_Grafica.MyApp(tipo_sensor="distancia", datos=self.historial.copy())
        else:
            # Actualizar los datos si ya existe
            self.ventana_grafica.actualizar_datos(self.historial.copy())
            self.ventana_grafica.tipo_sensor = "distancia"
            self.ventana_grafica.actualizar_titulo()

        # Mostrar la ventana
        self.ventana_grafica.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())