import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P04_SumaDosNumeros_V2.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_sumar.clicked.connect(self.sumar)

    def sumar(self):
        try:
            a = int(self.txt_A.text())
            b = int(self.txt_B.text())
            r = a+b
            #self.msj("La suma es: "+ str(r))
            self.txt_Resultado.setText(str(r))
        except Exception as error:
            print(error)

    def saludar (self):
        cadena = self.txt_nombre.text() ##se da en string, str, cadena, pss xd
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