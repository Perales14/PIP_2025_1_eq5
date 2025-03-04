import sys

from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "U2_E09_Parte2_Dadas_tres_opciones.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #botones = btn_1, btn_2, btn_3
        #poner esta en  a manera de diccionario en imagenes:

        imagenes = {#hacer un diccionario, el cual en cada elemento tendra 3 cosas, esas 3 cosas seran las posibles opciones, por lo que se tendra a si mismo el elemento.}


        }
        self.btn_Jugar.clicked.connect(self.jugar)
        self.btn_1.clicked.connect(self.opcion)
        self.btn_2.clicked.connect(self.opcion)
        self.btn_3.clicked.connect(self.opcion)

    def jugar(self):
        self.btn_1.setEnabled(True)

        self.btn_2.setEnabled(True)
        self.btn_3.setEnabled(True)
        self.lbl_Resultado.setText('')

    def opcion(self):
        send = self.sender()
        boton = send.objectName()[-1]

        print(boton)


    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
