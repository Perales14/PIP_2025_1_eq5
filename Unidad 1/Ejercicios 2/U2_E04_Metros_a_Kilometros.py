import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E04_Metros_a_Kilometros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Mk.clicked.connect(self.calcularKilometros)
        self.btn_Km.clicked.connect(self.calcularMetros)
        self.txt_Valor.textChanged.connect(self.CheckLetter)


    def calcularKilometros(self):
        if self.CheckValue():
            return

        metros = float(self.txt_Valor.text())
        kilometros = metros/1000

        self.lbl_ValorLongitud.setText(f"{round(kilometros, 3)} Kilómetros")
        self.lbl_Longitud.setText("Metros:")

    def calcularMetros(self):
        if self.CheckValue():
            return

        kilometros = float(self.txt_Valor.text())
        metros = kilometros * 1000

        self.lbl_ValorLongitud.setText(f"{round(metros, 3)} Metros")
        self.lbl_Longitud.setText("Kilómetros:")

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