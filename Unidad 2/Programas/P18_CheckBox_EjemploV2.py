import sys
import time as t
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "P17_ChechBox.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.cb_dormir.toggled.connect(self.control)
        self.cb_cine.toggled.connect(self.control)
        self.cb_jugar.toggled.connect(self.control)

    def dormir(self):
        valor = self.cb_dormir.isChecked()
        print(valor)

    def jugar(self):
        valor = self.cb_jugar.isChecked()
        print(valor)

    def control(self):
        obj = self.sender()#.objectName()
        valor = obj.isChecked()
        print("Objeto: ", obj.text(),valor)

    def cine(self):
        valor = self.cd_cine.isChecked()
        print(valor)

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