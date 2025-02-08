import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "E08_Velocidad.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Calcular.clicked.connect(self.calcular)
        self.txt_distancia.textChanged.connect(self.CheckLetterD)
        self.txt_tiempo.textChanged.connect(self.CheckLetterT)

    def calcular(self):
        try:
            distancia = float(self.txt_distancia.text())
            print(distancia)
            tiempo = float(self.txt_tiempo.text())
            print(tiempo)
        except:
            self.msj("Por favor, rellene ambos campos con distancias numericos")
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

    # def changeStyleSheet(self, label):
    #     label.setStyleSheet("""
    #        QLabel {
    #             text-decoration: underline;
    #             font: 20pt "Forte";
    #             color:rgb(0, 0, 0)
    #        }
    #        """)
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
    def CheckLetterD(self):
        distancia = self.txt_distancia.text()
        try:
            float(distancia)
            distancia = "".join(distancia.split())
            self.txt_distancia.setText(distancia)

        except:
            QtWidgets.QToolTip.showText(self.txt_distancia.mapToGlobal(self.txt_distancia.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_distancia.setFocus()
            distancia = distancia[:-1]
            self.txt_distancia.setText(distancia)
    def CheckLetterT(self):
        tiempo = self.txt_tiempo.text()
        try:
            float(tiempo)
            tiempo = "".join(tiempo.split())
            self.txt_tiempo.setText(tiempo)

        except:
            QtWidgets.QToolTip.showText(self.txt_tiempo.mapToGlobal(self.txt_tiempo.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_tiempo.setFocus()
            tiempo = tiempo[:-1]
            self.txt_tiempo.setText(tiempo)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())