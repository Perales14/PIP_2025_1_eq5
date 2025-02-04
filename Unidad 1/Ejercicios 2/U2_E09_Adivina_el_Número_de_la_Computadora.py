import sys
from PyQt5 import uic, QtWidgets, QtCore
import random
qtCreatorFile = "U2_E09_Adivina_el_Número_de_la_Computadora.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.valor = None
        self.setupUi(self)
        self.btn_Inicio.clicked.connect(self.Inicio)
        self.btn_Enviar.clicked.connect(self.Enviar)
        self.txt_Valor.textChanged.connect(self.CheckLetter)
        # El numero esta entre:

    def Inicio(self):
        if self.valor is None:
            self.valor = random.randint(1,100)
            self.lbl_Rango.setText(f"El numero esta entre {self.valor//10*10} y {self.valor//10*10+10}")
            # self.btn_Inicio.setText("Reiniciar")

        else:
            self.msj("Ya has iniciado el juego...")

        #sacar un numero aleatorio con Random
        # self.valor = random.randint(1,100)
        # #mostrar en lbl_Rango "el numero esta entre 1 y 10" segun su decena
        # self.lbl_Rango.setText(f"El numero esta entre {self.valor//10*10} y {self.valor//10*10+10}")



    def Enviar(self):
        if self.CheckValue():
            return
        try:
            valor = int(self.txt_Valor.text())

        except Exception as e:
            self.msj("Introduce un numero valido. ")
            return

        #3 casos, valordado es mayor, es menor y es igual
        if valor > self.valor:
            self.msj("El valor es menor")
        elif valor < self.valor:
            self.msj("El valor es mayor")
        else:
            self.msj("Felicidades, has adivinado el numero")
            self.valor = None




    def CheckValue(self):
        try:
            valorA = self.txt_Valor.text()
        except Exception as e:
            self.msj("Introduce un numero valido. ")
            
        if valorA == "":
            self.msj("Introduce un numero por favor.")
            return True
    def CheckLetter(self):
        valor = self.txt_Valor.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Valor.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Valor.mapToGlobal(self.txt_Valor.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Valor.setFocus()
            valor = valor[:-1]
            self.txt_Valor.setText(valor)

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())