import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E01_Grados_Centígrados_a_Fahrenheit.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.txt_Valor.textChanged.connect(self.ChechLetter)
        self.btn_Fc.clicked.connect(self.calcularCentigrados)
        self.btn_Cf.clicked.connect(self.calcularFahrenheit)

    def calcularFahrenheit(self):
        valor = self.txt_Valor.text()
        if valor == "":
            self.msj("Introduce un numero por favor.")
            return
        try:
            centigrados = float(valor)
            fahrenheit = centigrados * 9/5 + 32
        except Exception as e:
            self.msj("Se ha producido un error en la conversion")
            return
        self.lbl_ValorTemperatura.setText(f"{round(fahrenheit, 2)} Fahrenheit")
        self.lbl_Temperatura.setText("Centígrados:")

    def calcularCentigrados(self):
        valor = self.txt_Valor.text()
        if valor == "":
            self.msj("Introduce un numero por favor.")
            return
        try:
            fahrenheit = float(valor)
            centigrados = (fahrenheit - 32)/1.8
        except Exception as e:
            self.msj("Se ha producido un error en la conversion")
            return
        self.lbl_ValorTemperatura.setText(f"{round(centigrados, 2)} Centígrados")
        self.lbl_Temperatura.setText("Fahrenheit:")

    def ChechLetter(self):
        valor = self.txt_Valor.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Valor.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Valor.mapToGlobal(self.txt_Valor.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Valor.setFocus()
            print(valor)
            valor = valor[:-1]
            print(valor)
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