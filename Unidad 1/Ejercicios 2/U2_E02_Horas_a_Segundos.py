import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "U2_E02_Horas_a_Segundos.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Hs.clicked.connect(self.calcularSegundos)
        self.btn_Sh.clicked.connect(self.calcularHoras)
        self.txt_Valor.textChanged.connect(self.CheckLetter)

    def calcularSegundos(self):
        if self.CheckValue():
            return
        print("a")

        horas = float(self.txt_Valor.text())
        segundos = horas * 3600

        self.lbl_ValorTiempo.setText(f"{round(segundos, 2)} Segundos")
        self.lbl_Tiempo.setText("Horas:")

    def calcularHoras(self):
        if self.CheckValue():
            return
        print("asd")
        segundos = float(self.txt_Valor.text())
        horas = segundos/3600

        self.lbl_ValorTiempo.setText(f"{round(horas, 2)} Horas")
        self.lbl_Tiempo.setText("Segundos:")

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