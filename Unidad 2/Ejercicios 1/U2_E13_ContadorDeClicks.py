import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E13_ContadorDeClicksV2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_Temporizador.clicked.connect(self.temporizar2doPlano)
        self.btn_Clicks.clicked.connect(self.contadorClicks)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)

        self.txt_Segundos.textChanged.connect(self.CheckLetterS)

        self.valorN = -1
        self.contador = 0

    def controlSegundoPlano(self):
        self.txt_Segundos.setText(str(self.valorN))
        self.valorN -= 1

        if self.valorN == -1:
            self.segundoPlano.stop()
            self.btn_Clicks.setEnabled(False)
        pass

    def temporizar2doPlano(self):
        self.valorN = int(self.txt_Segundos.text())
        self.segundoPlano.start(1000)
        self.btn_Clicks.setEnabled(True)

    def contadorClicks(self):
        self.contador += 1
        self.lbl_Num_Clicks.setText(f"Número de clicks: {str(self.contador)}")

    def CheckLetterS(self):
        segundos = self.txt_Segundos.text()
        try:
            float(segundos)
            segundos = "".join(segundos.split())
            self.txt_Segundos.setText(segundos)

        except:
            QtWidgets.QToolTip.showText(self.txt_Segundos.mapToGlobal(self.txt_Segundos.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Segundos.setFocus()
            segundos = segundos[:-1]
            self.txt_Segundos.setText(segundos)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())