import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "E03_PuntoMedio_2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #para agregar la funcionalidad de calcular al boton de calcular
        self.btn_Calcular.clicked.connect(self.calcular)
        self.txt_X1.textChanged.connect(self.CheckLetterx1)
        self.txt_X2.textChanged.connect(self.CheckLetterx2)
        self.txt_Y1.textChanged.connect(self.CheckLettery1)
        self.txt_Y2.textChanged.connect(self.CheckLettery2)

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

    def CheckLetterx1(self):
        valor = self.txt_X1.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_X1.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_X1.mapToGlobal(self.txt_X1.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_X1.setFocus()
            valor = valor[:-1]
            self.txt_X1.setText(valor)

    def CheckLetterx2(self):
        valor = self.txt_X2.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_X2.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_X2.mapToGlobal(self.txt_X2.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_X2.setFocus()
            valor = valor[:-1]
            self.txt_X2.setText(valor)

    def CheckLettery1(self):
        valor = self.txt_Y1.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Y1.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Y1.mapToGlobal(self.txt_Y1.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Y1.setFocus()
            valor = valor[:-1]
            self.txt_Y1.setText(valor)

    def CheckLettery2(self):
        valor = self.txt_Y2.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            self.txt_Y2.setText(valor)

        except:
            QtWidgets.QToolTip.showText(self.txt_Y2.mapToGlobal(self.txt_Y2.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Y2.setFocus()
            valor = valor[:-1]
            self.txt_Y2.setText(valor)

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