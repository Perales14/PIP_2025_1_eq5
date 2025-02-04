import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E05_Pesos_a_Dolares.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Pd.clicked.connect(self.calcularDolares)
        self.btn_Dp.clicked.connect(self.calcularPesos)
        self.txt_Valor.textChanged.connect(self.CheckLetter)

    def calcularDolares(self):
        if self.CheckValue():
            return

        pesos = float(self.txt_Valor.text())
        dolares = pesos/20.44

        self.lbl_ValorMonetario.setText(f"{round(dolares, 2)} Dólares(USA$)")
        self.lbl_Monetario.setText("Peso(MxN):")

    def calcularPesos(self):
        if self.CheckValue():
            return

        dolares = float(self.txt_Valor.text())
        pesos = dolares * 20.44

        self.lbl_ValorMonetario.setText(f"{round(pesos, 2)} Pesos(MxN)")
        self.lbl_Monetario.setText("Dólares(USA$):")

    def CheckValue(self):
        valor = self.txt_Valor.text()
        if valor == "":
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