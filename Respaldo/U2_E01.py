import sys
from PyQt5 import uic, QtWidgets, QtCore
# import PyQt5
qtCreatorFile = "U2_E01_Grados_Centígrados_a_Fahrenheit.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Cf.clicked.connect(self.Cf)
        self.btn_Fc.clicked.connect(self.Fc)
        self.txt_Valor.textChanged.connect(self.ChechLetter)

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
            # self.txt_Valor.setText(valor.substring(0, len(valor)-1))
            # print("paso el tool")
            # try:
            #
            # except Exception as e:
            #     print(e)

            # self.msj("Solo se permiten números")

    def changeStyleSheet(self, label):
        label.setStyleSheet("""
           QLabel {
                text-decoration: underline;
                font: 20pt "Forte";
                color:rgb(0, 0, 0)
           }
           """)

    # def mostrar_error(self):
    #     mensaje = QtWidgets.QToolTip()
    #     mensaje.setIcon(QtWidgets.QToolTip.Critical)
    #     mensaje.setText("¡Error! Solo se permiten números.")
    #     mensaje.setWindowTitle("Entrada inválida")
    #     mensaje.exec_()

    def Cf(self):
        try:
            c = float(self.txt_Valor.text())
            f = (c*9/5)+32
            self.lbl_ValorTemperatura.setText(str(f))
        except:
            self.msj("Error en la conversión")

    def Fc(self):
        pass


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