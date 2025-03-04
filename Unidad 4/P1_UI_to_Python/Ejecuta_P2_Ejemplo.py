import sys
from PyQt5 import  QtWidgets
# qtCreatorFile = "P04_SumaDosNumeros.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

import P2_vPython_Ejemplo as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        #self.btn_saludar.clicked.connect(self.saludar)
        # self.btn_sumar.clicked.connect(self.sumar)
        self.btn_sumar.clicked.connect(self.sumar)

    # arquitectura, base de datos, framework.costos derivados
    # para poder darle los costos derivados.
    # si se va a usar SQL server, ver costos, en nuestro caso Supabase, cuales son los costos que puedan generar.
    # cosas que van a generar costo, decirle
    # tambien tener en cuenta los servicios que vamos a ofrecer despues de la entrega del proyecto.
    # ya sea sobre auditoria, y no se cuales cosas mas dijo
    def sumar(self):
        # C = self.txt_C.text()
        # print(C)
        try:
            a = int(self.txt_A.text())
            b = int(self.txt_B.text())
            C = int(self.txt_C.text())
            r = a+b + C
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
