import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E06_Area_Pentagono.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Area.clicked.connect(self.calcularArea)
        self.txt_ValorApotema.textChanged.connect(self.CheckLetterA)
        self.txt_ValorPerimetro.textChanged.connect(self.CheckLetterP)


    def calcularArea(self):
        if self.CheckValue():
            return

        apotema = float(self.txt_ValorApotema.text())
        perimetro = float(self.txt_ValorPerimetro.text())

        self.lbl_ValorSuperficie.setText(f"Área: {round((perimetro * apotema)/2, 2)}m2")

    def CheckValue(self):
        valorA = self.txt_ValorApotema.text()
        valueP = self.txt_ValorPerimetro.text()
        if valorA == "" or valueP == "":
            self.msj("Introduce un numero por favor.")
            return True
    def CheckLetterA(self):
        valor = self.txt_ValorApotema.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_ValorApotema.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_ValorApotema.mapToGlobal(self.txt_ValorApotema.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_ValorApotema.setFocus()
            valor = valor[:-1]
            self.txt_ValorApotema.setText(valor)


    def CheckLetterP(self):
        valor = self.txt_ValorPerimetro.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_ValorPerimetro.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_ValorPerimetro.mapToGlobal(self.txt_ValorPerimetro.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_ValorPerimetro.setFocus()
            valor = valor[:-1]
            self.txt_ValorPerimetro.setText(valor)

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())