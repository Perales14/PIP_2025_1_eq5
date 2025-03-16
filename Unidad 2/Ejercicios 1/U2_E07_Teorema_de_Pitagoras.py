import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E07_Teorema_de_Pitagoras.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Calcular.clicked.connect(self.calcularHipotenusa)
        self.txt_Valor.textChanged.connect(self.CheckLetterA)
        self.txt_Valor_2.textChanged.connect(self.CheckLetterB)


    def calcularHipotenusa(self):
        if self.CheckValue():
            return
        valor_A = float(self.txt_Valor.text())
        valor_B = float(self.txt_Valor_2.text())
        H2 = (valor_A**2 + valor_B**2)
        H = H2**0.5
        self.lbl_Hipotenusa.setText(f"Hipotenusa: {round(H,2)}")

    def CheckValue(self):
        valorA = self.txt_Valor.text()
        valueB = self.txt_Valor_2.text()
        if valorA == "" or valueB == "":
            self.msj("Introduce un numero por favor.")
            return True
    def CheckLetterA(self):
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


    def CheckLetterB(self):
        valor = self.txt_Valor_2.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Valor_2.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Valor_2.mapToGlobal(self.txt_Valor_2.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Valor_2.setFocus()
            valor = valor[:-1]
            self.txt_Valor_2.setText(valor)

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())