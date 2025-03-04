import sys
from PyQt5 import uic, QtWidgets

# qtCreatorFile = "P04_SumaDosNumeros.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

import P1_vPython_Ejemplo as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        #self.btn_saludar.clicked.connect(self.saludar)
        # self.btn_sumar.clicked.connect(self.sumar)
        self.btn_sumar.clicked.connect(self.sumar)

    def sumar(self):
        try:
            a = int(self.txt_A.text())
            b = int(self.txt_B.text())
            r = a+b
            self.msj("La suma es: "+ str(r))
        except Exception as error:
            print(error)

    def saludar (self):
        # cadena = self.txt_nombre.text() ##se da en string, str, cadena, pss xd
        cadena = "LUIS"
        if cadena != "":
            self.msj("SALUDOS, " +cadena+", Buen Dia")
        else:
            self.msj("Debes de ingresar tu nombre")

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)

        m.exec_()

    #Area de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
