import sys
from PyQt5 import uic, QtWidgets,QtGui, QtCore
qtCreatorFile = "PP02_CompuertasLogicasV.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.compuertaactiva = ''
        self.botones = [self.btn_and, self.btn_buffer, self.btn_nand, self.btn_not, self.btn_or, self.btn_xor, self.btn_xnor, self.btn_nor]
        for i in self.botones:
            i.clicked.connect(self.compuerta)
        self.lineEdit_A.textChanged.connect(self.CheckLetter)
        self.lineEdit_B.textChanged.connect(self.CheckLetter)

    def compuerta(self):
        self.compuertaactiva = self.sender().text()
        self.lbl_CompuertaActiva.setText('Compuerta Activa: '+self.compuertaactiva)
        self.actualizar()

    def actualizar(self):

        a = self.lineEdit_A.text()
        b = self.lineEdit_B.text()
        if a == '' or b == '':
            print('No hay valores')
            return
        if self.compuertaactiva == '':
            print('No hay compuerta')
            return
        a = bool(int(a))
        b = bool(int(b))
        if self.compuertaactiva == 'AND':
            self.lbl_Resultado.setText('Resultado: '+str(self.and_(a, b)))
        elif self.compuertaactiva == 'BUFFER':
            self.lbl_Resultado.setText('Resultado: '+str(self.buffer(a, b)))
        elif self.compuertaactiva == 'NAND':
            self.lbl_Resultado.setText('Resultado: '+str(self.nand(a, b)))
        elif self.compuertaactiva == 'NOT':
            self.lbl_Resultado.setText('Resultado: '+str(self.not_(a, b)))
        elif self.compuertaactiva == 'OR':
            self.lbl_Resultado.setText('Resultado: '+str(self.or_(a, b)))
        elif self.compuertaactiva == 'XOR':
            self.lbl_Resultado.setText('Resultado: '+str(self.xor(a, b)))
        elif self.compuertaactiva == 'XNOR':
            self.lbl_Resultado.setText('Resultado: '+str(self.xnor(a, b)))
        elif self.compuertaactiva == 'NOR':
            self.lbl_Resultado.setText('Resultado: '+str(self.nor(a, b)))

    def and_(self, a, b):
        return a and b
    def buffer(self, a, b):
        return a
    def nand(self, a, b):
        return not(a and b)
    def not_(self, a, b):
        return not a
    def or_(self, a, b):
        return a or b
    def xor(self, a, b):
        return a ^ b
    def xnor(self, a, b):
        return not(a ^ b)
    def nor(self, a, b):
        return not(a or b)

    def CheckLetter(self):
        send = self.sender()
        valor = send.text()
        try:
            valor = int(valor)
            if valor != 0 and valor != 1:
                QtWidgets.QToolTip.showText(send.mapToGlobal(send.rect().bottomLeft()),
                                            "Solo se permiten valores entre 0 y 1", None, QtCore.QRect(), 5000)
                send.setFocus()
                valor = str(valor)[:-1]
                send.setText(str(valor))
            else:
                valor = str(valor)
                send.setText(valor)
                self.actualizar()
        except:
            QtWidgets.QToolTip.showText(send.mapToGlobal(send.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            send.setFocus()
            valor = valor[:-1]
            send.setText(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())