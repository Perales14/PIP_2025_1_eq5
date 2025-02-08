import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "E01_IMC.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #para agregar la funcionalidad de calcular al boton de calcular
        self.btn_Calcular.clicked.connect(self.calcular)
        self.txt_Peso.textChanged.connect(self.CheckLetter)
        self.txt_Altura.textChanged.connect(self.CheckLetterA)

    def calcular(self):
        try:
            peso = float(self.txt_Peso.text())
            altura = float(self.txt_Altura.text())
        except:
            #por si dejan espacios, o ponen letras
            self.msj("Por favor, rellene ambos campos con valores numericos")
            return
        IMC = round(peso / (altura * altura),2)
        self.Lbl_IMC.setText("IMC: "+str(IMC))
        self.changeStyleSheet(self.Lbl_IMC)

    def changeStyleSheet(self, label):
        # cambia el stylesheet de un label
        label.setStyleSheet("""
           QLabel {
                text-decoration: underline;
                font: 20pt "Forte";
                color:rgb(0, 0, 0)
           }
           """)

    def CheckLetter(self):
        valor = self.txt_Peso.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Peso.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Peso.mapToGlobal(self.txt_Peso.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Peso.setFocus()
            valor = valor[:-1]
            self.txt_Peso.setText(valor)

    def CheckLetterA(self):
        valor = self.txt_Altura.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Altura.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Altura.mapToGlobal(self.txt_Altura.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Altura.setFocus()
            valor = valor[:-1]
            self.txt_Altura.setText(valor)

    def msj(self,txt):
        # muestra un mensaje en un MessageBox, la ventana asi chica de mensajes de alerta
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.setStyleSheet("""
                QMessageBox QLabel {
                    font-family: Arial;
                    font-size: 20px;
                    color: #123456;
                    font-weight: bold;
                }
            """)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())