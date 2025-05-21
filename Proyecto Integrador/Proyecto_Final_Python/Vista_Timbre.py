import sys
from PyQt5 import uic, QtWidgets, QtCore
import Vista_Grafica

qtCreatorFile = "Vista_Timbre.ui"
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
        self.timbre_dato = 0  # 0: no presionado, 1: presionado
        self.estado = 0  # 0: buzzer apagado, 1: buzzer encendido

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
        if self.parent and hasattr(self.parent, 'timbre_dato'):
            # Si hay referencia a la ventana principal, obtener datos de ahí
            self.timbre_dato = self.parent.timbre_dato
            self.estado = self.parent.buzzer_estado
            if hasattr(self.parent, 'historial_timbre'):
                self.historial = self.parent.historial_timbre.copy()
        else:
            # En caso contrario, simular localmente
            import random
            self.timbre_dato = random.randint(0, 1)
            self.estado = self.timbre_dato  # El estado del buzzer es igual al del timbre

            # Actualizar historial
            self.historial.append(self.timbre_dato)
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
        self.listWidget.addItem(f"Estado del timbre: {'Presionado' if self.timbre_dato else 'No presionado'}")
        self.listWidget.addItem(f"Estado del buzzer: {'Encendido' if self.estado else 'Apagado'}")

        # Agregar información adicional
        if self.timbre_dato:
            self.listWidget.addItem("¡Alguien está en la puerta!")
        else:
            self.listWidget.addItem("No hay nadie en la puerta")

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
            self.ventana_grafica = Vista_Grafica.MyApp(tipo_sensor="timbre", datos=self.historial.copy())
        else:
            # Actualizar los datos si ya existe
            self.ventana_grafica.actualizar_datos(self.historial.copy())
            self.ventana_grafica.tipo_sensor = "timbre"
            self.ventana_grafica.actualizar_titulo()

        # Mostrar la ventana
        self.ventana_grafica.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())