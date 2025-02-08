import sys
import time as t
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "P10_SegundoPlanoTimer.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control2doPlano)
        self.btn_temporizar.clicked.connect(self.temporizar2doPlano)
        self.valorN = -1

    def control2doPlano(self):
        self.txt_Valor.setText(str(self.valorN))
        self.valorN -= 1
        if self.valorN == -1:
            self.segundoPlano.stop()

    def temporizar2doPlano(self):
        self.valorN = int(self.txt_Valor.text())
        self.segundoPlano.start(500)

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