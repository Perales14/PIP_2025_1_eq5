import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E03_Mililitros_a_Litros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Ml.clicked.connect(self.calcularLitros)
        self.btn_Lm.clicked.connect(self.calcularMililitros)
        self.txt_Valor.textChanged.connect(self.CheckLetter)

    def calcularLitros(self):
        if self.CheckValue():
            return

        mililitros = float(self.txt_Valor.text())
        litros = mililitros/1000

        self.lbl_ValorCapacidad.setText(f"{round(litros, 2)} Litros")
        self.lbl_Capacidad.setText("Mililitros:")

    def calcularMililitros(self):
        if self.CheckValue():
            return

        litros = float(self.txt_Valor.text())
        mililitros = litros*1000

        self.lbl_ValorCapacidad.setText(f"{round(mililitros, 2)} Mililitros")
        self.lbl_Capacidad.setText("Litros:")

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