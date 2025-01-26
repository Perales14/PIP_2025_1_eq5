import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E07_Promedio_5.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
valores = []
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Calcular.clicked.connect(self.calcular)
        self.btn_AgregarValor.clicked.connect(self.agregarValor)


    def agregarValor(self):
        if len(valores) == 5:
            self.msj("No se pueden agregar mas valores")
            return
        try:
            valor = float(self.txt_Valor.text())
        except:
            self.msj("Por favor, rellene el campo con valores numericos")
            return
        if len(valores) == 4:
            self.msj("Ya se han ingresado todos los valores")
        valores.append(valor)
        self.txt_Valor.setText("")
        self.txt_Valor.setFocus()

    def calcular(self):
        suma = 0
        for n in valores:
            suma += n
        promedio = suma / 5
        self.Lbl_promedio.setText(f"Promedio: {promedio}")
        # self.changeStyleSheet(self.Lbl_promedio)
        self.Lbl_promedio.setStyleSheet("""
            QLabel {
                text-align: center; 
                text-decoration: underline;
                font: 20pt "Forte";
                color:rgb(0, 0, 0);
                qproperty-alignment: 'AlignCenter'; 
            }
            """)
        valores.clear()


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