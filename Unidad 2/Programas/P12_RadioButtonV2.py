import sys
import time as t
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "P12_RadioButtonV2.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.rb_perro.clicked.connect(self.perro)
        self.rb_gato.clicked.connect(self.gato)
        self.rb_hamster.clicked.connect(self.hamster)

        self.rb_negro.toggled.connect(self.negro)
        self.rb_rojo.toggled.connect(self.rojo)
        self.rb_azul.toggled.connect(self.azul)

    def negro(self):
        v = self.rb_negro.isChecked()
        print('negro',v)

    def rojo(self):
        v = self.rb_rojo.isChecked()
        print('rojo',v)

    def azul(self):
        v = self.rb_azul.isChecked()
        print('azul',v)

    def perro(self):
        print('perro')

    def gato(self):
        print('gato')

    def hamster(self):
        print('hamster')

    def msj(self, mensaje):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle("Advertencia")
        msg.exec_()

    # def temporizar(self):
    #     print('temporizar')
    #     valor = int(self.txt_Valor.text())
    #     print(valor)
    #     for i in range(valor,0,-1):
    #         self.txt_Valor.setText(str(i))
    #         print(i)
    #         t.sleep(0.5)

#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())