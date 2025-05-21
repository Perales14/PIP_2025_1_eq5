import sys
from PyQt5 import uic, QtWidgets

import serial as tarjeta

qtCreatorFile = "P35_ArduinoPythonGUI.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)

    def accion(self):
        texto = self.btn_accion.text()
        com = self.txt_com.text()
        if texto == "CONECTAR":
            print(1)
            self.arduino = tarjeta.Serial(com,baudrate=9600,timeout=1)
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
        elif texto == "DESCONECTAR":
            print(2)
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
        elif texto == "RECONECTAR":
            print(3)
            self.arduino.open()
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")


#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

#hacer los otros de los ejercicios,
# hacer comentarios en los ejercicios
# poner la conclusion de lo aprendido, sobre comportamientos y eso.
# cual consideramos que es la mejor para X o Y cosa