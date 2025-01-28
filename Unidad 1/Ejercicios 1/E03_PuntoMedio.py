import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E03_PuntoMedio_2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #para agregar la funcionalidad de calcular al boton de calcular
        self.btn_Calcular.clicked.connect(self.calcular)

    def calcular(self):
        try:
            x1 = float(self.txt_X1.text())
            y1 = float(self.txt_Y1.text())
            x2 = float(self.txt_X2.text())
            y2 = float(self.txt_Y2.text())

        except:
            #por si dejan espacios, o ponen letras
            self.msj("Por favor, rellene ambos campos con valores numericos")
            return
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2
        final = f"\n({xm}, {ym})"

        self.Lbl_pm.setText("Punto Medio: "+final)

    def changeStyleSheet(self, label):
        # cambia el stylesheet de un label
        label.setStyleSheet("""
           QLabel {
                text-decoration: underline;
                font: 20pt "Forte";
                color:rgb(0, 0, 0);
                text-align: top;
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