import sys

from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "U2_E06_Parte2_TIC_TAC_TOE_GATO.ui" # Nombre del archivo aqui
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
        self.gato = True
        self.botones = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
        self.tabla = {'A':[0,0,0],'B':[0,0,0],'C':[0,0,0]}
        self.contador = 0
        a = self.A1
        print(a.objectName())
        for i in self.botones:
            btn = self.findChild(QtWidgets.QToolButton,i)
            print('btn')
            print(btn)
            #encuentra boton con nombre "i", lo trae a "btn" y le asigna la funcion "cambiar"
            btn.clicked.connect(self.cambiar)
            btn.setEnabled(False)
        #:/Ejercicios/Equis.png
        # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Equis.png"))
        self.cambiaropcion('EquisG_1')
        #por defecto
        self.btn_Jugar.clicked.connect(self.jugar)
        self.btn_Circulo.clicked.connect(self.ficha)
        self.btn_Equis.clicked.connect(self.ficha)

    def jugar(self):
        self.contador = 0
        for i in self.botones:
            btn = self.findChild(QtWidgets.QToolButton,i)
            btn.setIcon(QtGui.QIcon(""))
            btn.setEnabled(True)
        self.cambiarestado(False)
        for i in ['A','B','C']:
            for j in range(3):
                self.tabla[i][j] = ''

        if self.gato:
            self.cambiaropcion('EquisG_1')
            # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Equis.png"))
            # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Equis.png"))
        else:
            self.cambiaropcion('Circulo')
            # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Circulo.png"))
            # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Circulo.png"))
        #
        # self.gato = True

    def ficha(self):
        send = self.sender()
        if send == self.btn_Circulo:
            self.gato = True
            self.cambiaropcion('EquisG_1')
            # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Equis.png"))
        else:
            self.gato = False
            self.cambiaropcion('Circulo')
            # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Circulo.png"))

    def cambiar(self):

        send = self.sender()
        nombre = send.objectName()
        self.contador += 1
        if self.gato:
            #si es el turno del gato
            send.setIcon(QtGui.QIcon(":/Ejercicios/Equis.png"))
            self.tabla[nombre[0]][int(nombre[1])-1] = 'Gato'
        else:
            #si es el turno del raton
            send.setIcon(QtGui.QIcon(":/Ejercicios/Circulo.png"))
            self.tabla[nombre[0]][int(nombre[1])-1] = 'Raton'
        jugador = 'Gato' if self.gato else 'Raton'
        self.gato = not self.gato
        send.setEnabled(False)
        if self.evaluarGanador(jugador):
            self.msj(f"El jugador {jugador} ha ganado")
            # self.jugar()
            self.cambiarestado(True)
            for i in self.botones:
                btn = self.findChild(QtWidgets.QToolButton,i)
                btn.setEnabled(False)
            self.gato = True

            return
        if self.contador == 9:
            self.msj("Empate")
            # self.jugar()
            self.cambiarestado(True)
            for i in self.botones:
                btn = self.findChild(QtWidgets.QToolButton,i)
                btn.setEnabled(False)
            return
        # self.lbl_OpcionElegida.setPixmap(QtGui.QPixmap(":/Ejercicios/Equis.png") if self.gato else QtGui.QPixmap(":/Ejercicios/Circulo.png"))
        self.cambiaropcion('EquisG_1' if self.gato else 'Circulo')

    def cambiaropcion(self,opcion):
        self.lbl_OpcionElegida.setStyleSheet("image: url(:/Ejercicios/"+opcion+".png);")

    def cambiarestado(self,bool):
        self.btn_Jugar.setEnabled(bool)
        self.btn_Circulo.setEnabled(bool)
        self.btn_Equis.setEnabled(bool)

    def evaluarGanador(self,jugador):
        #ver si hay un ganador.
        print('self.tabla')
        print(self.tabla)
        print(jugador)
        if self.tabla['A'][0] == self.tabla['B'][1] == self.tabla['C'][2] == jugador:
            return True
        if self.tabla['A'][2] == self.tabla['B'][1] == self.tabla['C'][0] == jugador:
            return True
        for columna in range(3):
            if self.tabla['A'][columna] == self.tabla['B'][columna] == self.tabla['C'][columna] == jugador:
                return True
        for fila in ['A','B','C']:
            if self.tabla[fila][0] == self.tabla[fila][1] == self.tabla[fila][2] == jugador:
                return True
        return False

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
