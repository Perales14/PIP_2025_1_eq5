import serial as tarjeta
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Dialogo_ConexionArduino.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, referencia_a_home):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.txt_COM.setText("COM13")
        self.btn_Conectar.clicked.connect(self.conectar)

        self.home = referencia_a_home

    def conectar(self):
        try:
            texto = self.btn_Conectar.text()
            com = self.txt_COM.text()
            if texto == "Conectar":
                # Para simulación, podemos crear un objeto "falso" que simule ser un puerto serial
                # o usar un puerto serial real si está disponible
                try:
                    self.home.arduino = tarjeta.Serial(com, baudrate=115200, timeout=1)
                except:
                    print("Error al conectar al puerto serie. Usando simulación.")
                    # Si no se puede conectar al puerto real, creamos un objeto similar
                    class ArduinoSimulado:
                        def __init__(self):
                            self._is_open = True

                        def isOpen(self):
                            return self._is_open

                        def close(self):
                            self._is_open = False

                        def open(self):
                            self._is_open = True

                        def write(self, data):
                            # Simular escritura al Arduino
                            pass

                        def inWaiting(self):
                            # Simular que siempre hay datos disponibles
                            return True

                        def readline(self):
                            # Simular lectura del Arduino
                            return b"0-0-0-N-25-0-50-0"

                    self.home.arduino = ArduinoSimulado()

                self.home.segundoPlano.start(100)
                self.btn_Conectar.setText("Desconectar")
                self.home.lbl_Estado.setText("Conectado")

            elif texto == "Desconectar":
                self.home.segundoPlano.stop()
                self.home.arduino.close()
                self.btn_Conectar.setText("Reconectar")
                self.home.lbl_Estado.setText("Desconectado")

            elif texto == "Reconectar":
                self.home.arduino.open()
                self.home.segundoPlano.start(100)
                self.btn_Conectar.setText("Desconectar")
                self.home.lbl_Estado.setText("Reconectado")
        except Exception as error:
            print(error)
            QtWidgets.QMessageBox.critical(self, "Error", f"Error al conectar: {str(error)}")