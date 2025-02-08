import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "E09_Voltaje_Ley_OHM.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #para agregar la funcionalidad de calcular al boton de calcular
        self.btn_Calcular.clicked.connect(self.calcular)
        self.txt_Resistencia.textChanged.connect(self.CheckLetterR)
        self.txt_Intensidad.textChanged.connect(self.CheckLetterI)

    def calcular(self):
        try:
            resistencia = float(self.txt_Resistencia.text())
            intensidad = float(self.txt_Intensidad.text())
        except Exception as error:
            #por si dejan espacios, o ponen letras
            print(error)
            self.msj("Por favor, rellene ambos campos con valores numericos")
            return
        voltaje = round(resistencia * intensidad,1)

        self.Lbl_Voltaje.setText("Voltaje: "+str(voltaje)+" V")
        self.changeStyleSheet(self.Lbl_Voltaje)
        # self.Lbl_Area.setText("Area: "+str(area))
        # self.changeStyleSheet(self.Lbl_Area)

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
    def CheckLetterR(self):
        resistencia = self.txt_Resistencia.text()
        try:
            float(resistencia)
            resistencia = "".join(resistencia.split())
            self.txt_Resistencia.setText(resistencia)

        except:
            QtWidgets.QToolTip.showText(self.txt_Resistencia.mapToGlobal(self.txt_Resistencia.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Resistencia.setFocus()
            resistencia = resistencia[:-1]
            self.txt_Resistencia.setText(resistencia)
    def CheckLetterI(self):
        intensidad = self.txt_Intensidad.text()
        try:
            float(intensidad)
            intensidad = "".join(intensidad.split())
            self.txt_Intensidad.setText(intensidad)

        except:
            QtWidgets.QToolTip.showText(self.txt_Intensidad.mapToGlobal(self.txt_Intensidad.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Intensidad.setFocus()
            intensidad = intensidad[:-1]
            self.txt_Intensidad.setText(intensidad)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())