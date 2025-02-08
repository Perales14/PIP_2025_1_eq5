import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "E06_IVA.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #para agregar la funcionalidad de calcular al boton de calcular
        self.btn_Calcular.clicked.connect(self.calcular)
        self.txt_Cantidad.textChanged.connect(self.CheckLetterC)

    def calcular(self):
        try:
            cantidad = float(self.txt_Cantidad.text())
        except Exception as error:
            #por si dejan espacios, o ponen letras
            print(error)
            self.msj("Por favor, rellene ambos campos con valores numericos")
            return
        IVA = cantidad * 0.16
        total = cantidad + IVA
        self.Lbl_IVA.setText("IVA: "+str(IVA))
        self.changeStyleSheet(self.Lbl_IVA)
        self.Lbl_total.setText("Total: "+str(total))
        self.changeStyleSheet(self.Lbl_total)

    def changeStyleSheet(self, label):
        # cambia el stylesheet de un label
        label.setStyleSheet("""
           QLabel {
                text-decoration: underline;
                font: 20pt "Forte";
                color:rgb(0, 0, 0)
           }
           """)
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

    def CheckLetterC(self):
        valor = self.txt_Cantidad.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Cantidad.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Cantidad.mapToGlobal(self.txt_Cantidad.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Cantidad.setFocus()
            valor = valor[:-1]
            self.txt_Cantidad.setText(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())