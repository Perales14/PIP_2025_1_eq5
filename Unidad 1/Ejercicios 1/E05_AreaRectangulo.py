import sys
from PyQt5 import uic, QtWidgets, QtCore
archivo = "E05_AreaRectangulo.ui"
qtCreatorFile = archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        Ui_MainWindow.__init__(self)
        # Ui_MainWindow.
        self.setupUi(self)
        #para agregar la funcionalidad de calcular al boton de calcular
        self.btn_Calcular.clicked.connect(self.calcular)
        self.txt_Largo.textChanged.connect(self.CheckLetter)
        self.txt_Ancho.textChanged.connect(self.CheckLettera)

    def calcular(self):
        try:
            largo = float(self.txt_Largo.text())
            ancho = float(self.txt_Ancho.text())
        except Exception as error:
            #por si dejan espacios, o ponen letras
            print(error)
            self.msj("Por favor, rellene ambos campos con valores numericos")
            return
        area = largo * ancho
        self.Lbl_Area.setText("Area: "+str(area))
        self.changeStyleSheet(self.Lbl_Area)

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

    def CheckLetter(self):
        valor = self.txt_Largo.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Largo.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Largo.mapToGlobal(self.txt_Largo.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Largo.setFocus()
            valor = valor[:-1]
            self.txt_Largo.setText(valor)

    def CheckLettera(self):
        valor = self.txt_Ancho.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Ancho.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Ancho.mapToGlobal(self.txt_Ancho.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Ancho.setFocus()
            valor = valor[:-1]
            self.txt_Ancho.setText(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())