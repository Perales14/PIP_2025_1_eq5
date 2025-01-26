import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E08_Velocidad.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Calcular.clicked.connect(self.calcular)


    def calcular(self):
        try:
            distancia = float(self.txt_distancia.text())
            print(distancia)
            tiempo = float(self.txt_tiempo.text())
            print(tiempo)
        except:
            self.msj("Por favor, rellene ambos campos con valores numericos")
            return
        #si es mayor a 1km, lo mejor sera darla en Km/h
        if distancia >= 1000:
            distancia = distancia/1000
            velocidad = round(distancia/tiempo,2)

            velocidad = "Velocidad: "+str(velocidad)+" km/h"
        #si es menor a 1km, lo mejor sera darla en m/h
        else:
            velocidad = round(distancia/tiempo,2)
            velocidad = "Velocidad: "+str(velocidad)+" m/h"
        self.Lbl_Velocidad.setText(velocidad)

    def changeStyleSheet(self, label):
        label.setStyleSheet("""
           QLabel {
                text-decoration: underline;
                font: 20pt "Forte";
                color:rgb(0, 0, 0)
           }
           """)
    def msj(self,txt):
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