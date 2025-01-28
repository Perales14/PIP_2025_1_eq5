import sys
from PyQt5 import uic, QtWidgets
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())