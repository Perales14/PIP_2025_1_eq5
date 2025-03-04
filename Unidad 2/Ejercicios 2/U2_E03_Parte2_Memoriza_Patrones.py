from PyQt5 import uic, QtWidgets, QtCore
import sys
import random
qtCreatorFile = "U2_E03_Parte2_Memoriza_Patrones.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.orden = []
        self.botones = []
        self.indice = 1 #Indica en hasta que lugar del orden se le mostrara
        self.posicion = 0 #Indica en Que lugar del Orden se encuentra el usuario (Hasta donde ha llegado de manera correcta
        self.setupUi(self)
        self.botones = [self.findChild(QtWidgets.QPushButton,'btn_'+str(i+1)) for i in range(10)]
        for btn in self.botones:
            btn.clicked.connect(self.validarOrden)
        self.btn_Jugar.clicked.connect(self.jugar)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)
        # self.segundoPlano.start(500)
        self.tiempo = 1
        self.color = QtCore.QTimer()
        self.color.timeout.connect(self.t)
        self.Segundos = 0
        self.control = 0

    def t(self):
        if self.tiempo%2 !=0:
            # print('A') #nuvo color
            print('gris',self.orden[self.control - 1])

            self.botones[self.orden[self.control - 1]].setStyleSheet("""
                        font: 20pt "Forte";
                        background-color: rgb(100, 100, 100);
                        color: rgb(255, 255, 255);
                        border-radius:30px;
                        border:6px solid #B0BEC5;
                        """)
        else:
            print('rojo',self.orden[self.control - 1])
            # print('B')#regresa color
            self.botones[self.orden[self.control - 1]].setStyleSheet("""
                        font: 20pt "Forte";
                        background-color: rgb(130,0,2);
                        color: rgb(255, 255, 255);
                        border-radius:30px;
                        border:6px solid #B0BEC5;
                        """)
        self.tiempo -=1
        if self.tiempo ==-1:
            print('stop')
            self.color.stop()

    def controlSegundoPlano(self):

        self.tiempo = 1
        self.color.start(450)
        self.control +=1

        if self.control == self.segundos:
            self.segundoPlano.stop()

    def resaltarBoton(self, boton, color_presionado):
        estilo_original = boton.styleSheet()
        # Cambiar solo el color de fondo temporalmente
        boton.setStyleSheet(estilo_original + f"background-color: {color_presionado};")
        QtCore.QTimer.singleShot(200, lambda: boton.setStyleSheet(estilo_original))

    def validarOrden(self):
        send = self.sender()
        numero = send.objectName()[-1] #saber que numero presiono
        self.resaltarBoton(send, "rgb(100, 100, 100)")
        numero = int(numero)
        print('n0',numero)
        #Si el mero es el indicado, suma mas uno el indice
        print(self.orden[self.posicion]+1)
        if self.orden[self.posicion]+1 == numero:
            # self.indice += 1
            self.siguiente()
            # self.posicion += 1
        else:
            self.msj('Haz perdido, Intentalo de Nuevo. ')
            self.posicion = 0
            self.indice = 1
            self.mostrar(self.indice)
            return

    def jugar(self):
        self.orden = [int(i) for i in range(10) ]
        # print(00)
        for i in range(10):
            valor = random.choice(range(i,10))
            self.orden[i], self.orden[valor] = self.orden[valor],self.orden[i]

        self.indice = 1
        self.mostrar(1)

    def mostrar(self,indice):
        self.segundos = indice
        self.control = 0
        self.segundoPlano.start(1000)



    def siguiente(self):


        # print('ind',self.indice)
        if self.indice == 11:
            self.msj('Haz Ganado.')
            return

        if self.indice == self.posicion+1:
            self.msj('Correcto, ahora un nivel mas arriba')
            self.indice+=1
            self.mostrar(self.indice)
            self.posicion = 0
            return
        self.posicion+=1
        # Iniciar de nuevo la secuencia hasta "self Indice" y reiniciar self.indice al salir


    def msj(self,mensaje):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle("Mensaje")
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
