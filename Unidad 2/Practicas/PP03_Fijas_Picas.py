import sys,random
from PyQt5 import uic, QtWidgets,QtGui, QtCore
qtCreatorFile = "PP03_Fijas_PicasVV.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#Comando para crear el Recursos_rc.1.py, desde "archivos" y lo cree en esta carpeta, no alla
# pyrcc5 .\Recursos.qrc -o '..\Unidad 2\Recursos_rc.1.py'
# como tal el codigo es
#asi lo creara en la carpeta en la que se encuentre
# pyrcc5 .\Recursos.qrc -o Recursos_rc.1.py

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.numero = str(random.randint(1000,9999))
        print(self.numero)
        self.lista = []
        self.btn_jugar.clicked.connect(self.fijas)
        self.txt_valor.textChanged.connect(self.CheckLetter);
        # self.txt_Lista.setEnabled(False)

    # def jugar(self):


    def fijas(self):
        numero = self.txt_valor.text()

        if len(numero) !=4:
            self.msj("Ingresa un Numero Valido")
            return

        self.lista.append(numero)
        cadena = ''
        for i in self.lista:
            cadena += i+"\n"
        self.txt_Lista.setText(cadena)
        fija,pica = 0,0
        for i in [0,1,2,3]:
            # print('si pasa?')
            try:
                if numero[i] in self.numero:
                    print('Si esta  el numero')
                    if numero[i] == self.numero[i]:
                        fija += 1
                    else:
                        pica += 1
            except Exception as e:
                print(e)
        if fija == 4:
            self.msj("Ganaste")
            return
        self.txt_fijas.setText("Fijas: " + str(fija))
        self.txt_picas.setText("Picas: " + str(pica))

    def CheckLetter(self):
        enviador = self.sender()
        valor = enviador.text()
        try:
            float(valor)
            valor = "".join(valor.split())
            enviador.setText(valor)

        except:
            QtWidgets.QToolTip.showText(enviador.mapToGlobal(enviador.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            enviador.setFocus()
            valor = valor[:-1]
            enviador.setText(valor)

    def msj(self,mensaje):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle("Mensaje")
        msg.exec_()

#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())