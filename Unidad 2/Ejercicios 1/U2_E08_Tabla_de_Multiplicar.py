import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E08_Tabla_de_Multiplicar.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_CT.clicked.connect(self.CalcularTabla)
        self.txt_Valor.textChanged.connect(self.CheckLetter)


    def CalcularTabla(self):
        if self.CheckValue():
            return
        try:
            valor = int(self.txt_Valor.text())

        except Exception as e:
            self.msj("Introduce un numero valido. ")
            return

        resultado = [f"{valor} x {i} = {valor*i}" for i in   range(1,11)]
        self.lbl_Tabla.setText("\n".join(resultado))




    def CheckValue(self):
        valorA = self.txt_Valor.text()
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