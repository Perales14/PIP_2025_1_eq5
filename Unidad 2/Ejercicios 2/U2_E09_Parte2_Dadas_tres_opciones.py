import sys
import random

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = "U2_E09_Parte2_Dadas_tres_opciones.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.imagenes = {
            'manzana': ['manzana','pera','membrillo'],
            'mandarina': ['limon','naranja','mandarina'],
            'cilantro': ['perejil','cilantro','apio']
        }
        self.lista = ['manzana','mandarina','cilantro']
        self.btn_Jugar.clicked.connect(self.jugar)
        self.btn_1.clicked.connect(self.opcion)
        self.btn_2.clicked.connect(self.opcion)
        self.btn_3.clicked.connect(self.opcion)
        self.palabra = ''
        self.btn_1.setEnabled(False)
        self.btn_2.setEnabled(False)
        self.btn_3.setEnabled(False)

    def jugar(self):
        self.palabra = random.randint(0,2)
        self.lbl_imagen_2.setText('')
        self.lbl_imagen_2.setStyleSheet(f"image: url(:/Ejercicios/{self.lista[self.palabra]}.png);")
        self.btn_1.setEnabled(True)
        self.btn_2.setEnabled(True)
        self.btn_3.setEnabled(True)
        self.btn_1.setText(self.imagenes[self.lista[self.palabra]][0])
        self.btn_2.setText(self.imagenes[self.lista[self.palabra]][1])
        self.btn_3.setText(self.imagenes[self.lista[self.palabra]][2])


    def opcion(self):
        send = self.sender()
        if send.text() == self.lista[self.palabra]:
            self.msj('Correcto')
            self.jugar()
        else:
            self.msj('Incorrecto')


    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())