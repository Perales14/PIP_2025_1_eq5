import sys
from PyQt5 import uic, QtWidgets, QtCore
import Vista_Grafica

qtCreatorFile = "Vista_PuertaTrasera.ui"
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
        self.boton_matriz_input = "N"  # Entrada del botón matriz
        self.password = ""  # Contraseña ingresada
        self.contrasena_correcta = "1234"  # Contraseña por defecto
        self.estado = 0  # 0: cerrada, 1: abierta

        # Historial de mediciones para la gráfica (estado)
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
        if self.parent and hasattr(self.parent, 'boton_matriz_input'):
            # Si hay referencia a la ventana principal, obtener datos de ahí
            self.boton_matriz_input = self.parent.boton_matriz_input
            self.password = self.parent.boton_matriz_password
            self.estado = self.parent.puerta_trasera_estado
            if hasattr(self.parent, 'historial_puerta_trasera'):
                self.historial = self.parent.historial_puerta_trasera.copy()
        else:
            # En caso contrario, simular localmente
            import random
            botones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "#", "*", "N"]
            if random.random() < 0.1:  # 10% de probabilidad de cambiar
                self.boton_matriz_input = random.choice(botones)

                # Procesar entrada
                if self.boton_matriz_input == "#":
                    # Inicio de ingreso de contraseña
                    self.password = ""
                elif self.boton_matriz_input == "*":
                    # Fin de ingreso de contraseña, verificar
                    if self.password == self.contrasena_correcta:
                        self.estado = 1  # Abrir puerta
                    else:
                        self.estado = 0  # Mantener cerrada
                elif self.boton_matriz_input != "N":
                    # Agregar dígito a la contraseña
                    self.password += self.boton_matriz_input

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
        self.listWidget.addItem(f"Entrada actual: {self.boton_matriz_input}")
        self.listWidget.addItem(f"Contraseña ingresada: {'*' * len(self.password)}")
        self.listWidget.addItem(f"Estado de la puerta: {'Abierta' if self.estado else 'Cerrada'}")

        # Agregar información adicional
        if self.boton_matriz_input == "#":
            self.listWidget.addItem("Inicio de ingreso de contraseña")
        elif self.boton_matriz_input == "*":
            if self.password == self.contrasena_correcta:
                self.listWidget.addItem("Contraseña correcta - Puerta abierta")
            else:
                self.listWidget.addItem("Contraseña incorrecta - Puerta cerrada")
        elif self.boton_matriz_input != "N":
            self.listWidget.addItem(f"Tecla presionada: {self.boton_matriz_input}")
        else:
            self.listWidget.addItem("No se ha presionado ninguna tecla")

    def prender_apagar(self):
        if self.btn_Prender.text() == "Prender":
            self.estado = 1  # Abrir puerta
            self.btn_Prender.setText("Apagar")
            self.parent.puerta = False
            self.parent.puerta_trasera_estado = 1
        else:
            self.estado = 0  # Cerrar puerta
            self.parent.puerta = True
            self.parent.puerta_trasera_estado = 0
            self.btn_Prender.setText("Prender")

        # Si está activada la actualización de datos, actualizar ahora
        if self.mostrar_datos_activo:
            self.mostrar_datos()

    def visualizar_grafica(self):
        # Crear la ventana de gráfica si no existe
        if not self.ventana_grafica:
            self.ventana_grafica = Vista_Grafica.MyApp(tipo_sensor="puerta_trasera", datos=self.historial.copy())
        else:
            # Actualizar los datos si ya existe
            self.ventana_grafica.actualizar_datos(self.historial.copy())
            self.ventana_grafica.tipo_sensor = "puerta_trasera"
            self.ventana_grafica.actualizar_titulo()

        # Mostrar la ventana
        self.ventana_grafica.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())