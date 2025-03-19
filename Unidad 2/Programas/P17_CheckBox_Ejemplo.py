import sys
import time as t
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "P17_CheckBox_ejemplo.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.cb_dormir.clicked.connect(self.dormir)
        self.cb_cine.clicked.connect(self.cine)
        self.cb_jugar.clicked.connect(self.jugar)

    def dormir(self):
        valor = self.cb_dormir.isChecked()
        print(valor)

    def jugar(self):
        valor = self.cb_jugar.isChecked()
        print(valor)

    def cine(self):
        valor = self.cb_cine.isChecked()
        print(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())