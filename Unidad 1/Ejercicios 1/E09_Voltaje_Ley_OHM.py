import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E09_Voltaje_Ley_OHM.ui"
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
            resisntencia = float(self.txt_Resistencia.text())
            intensidad = float(self.txt_Intensidad.text())
        except Exception as error:
            #por si dejan espacios, o ponen letras
            print(error)
            self.msj("Por favor, rellene ambos campos con valores numericos")
            return
        voltaje = round(resisntencia * intensidad,1)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())