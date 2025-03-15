import random
import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "Proyecto_memorama.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.imagenes = {
            '0': ':/Ejercicios/Archivos/Adobe Express - file (1).png',
            '1': ':/Ejercicios/Archivos/export202502092135328918.png',
            '2': ':/Ejercicios/Archivos/export202502092235269890.png',
            '3': ':/Ejercicios/Archivos/export202502092210045727.png',
            '4': ':/Ejercicios/Archivos/export202502092201258300.png',
            '5': ':/Ejercicios/Archivos/export202502092116429107.png'
        }
        self.botones =[]
        for i in range(12):
            boton = self.findChild(QtWidgets.QToolButton, f'toolbtn_{i+1}')
            self.botones.append(boton)
            boton.clicked.connect(self.ficha)
            boton.setEnabled(False)
        self.btn_Jugar.clicked.connect(self.jugar)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.retorno)
        self.lista = []
        self.partida = {
            'juegos': 0,
            'intentos': 0,
            'fichas': 0
        }
        self.v_time = QtCore.QTimer()
        self.v_time.timeout.connect(self.volteo)
        self.presionados = [-1, -1]
        self.btn_Si.hide()
        self.btn_No.hide()
        self.lbl_Pregunta.hide()
        self.lbl_o.hide()
        self.btn_No.clicked.connect(self.no)
        self.btn_Si.clicked.connect(self.si)

    def volteo(self):
        self.botones[self.presionados[0]].setStyleSheet(
            '''
                            image: url(:/Ejercicios/EquisG_1.png);
                            color: rgb(255, 255, 255);
                            border-radius:30px;
                            border-radius:30px;
                            border:6px solid #B0BEC5;
                        '''
        )
        self.botones[self.presionados[1]].setStyleSheet(
            '''
                            image: url(:/Ejercicios/EquisG_1.png);
                            color: rgb(255, 255, 255);
                            border-radius:30px;
                            border-radius:30px;
                            border:6px solid #B0BEC5;
                        '''
        )

        self.presionados = [-1, -1]
        for i in self.botones:
            i.setEnabled(True)
            i.clicked.disconnect(self.espera)
            i.clicked.connect(self.ficha)
        self.v_time.stop()


    def espera(self):
        self.msj('Espera un momento por favor')

    def jugar(self):
        self.partida['juegos']+=1
        self.btn_Jugar.setEnabled(False)
        self.btn_Jugar.hide()
        self.lista = self.mix()
        for i in range(12):
            self.botones[i].setStyleSheet(
                f'''
                    image: url({self.imagenes[f'{self.lista[i]%6}']});
                    color: rgb(255, 255, 255);
                    border-radius:30px;
                    border-radius:30px;
                    border:6px solid #B0BEC5;
                '''
            )
        self.timer.start(2000)


    def retorno(self):
        for i in self.botones:
            i.setStyleSheet(
                '''
                                image: url(:/Ejercicios/EquisG_1.png);
                                color: rgb(255, 255, 255);
                                border-radius:30px;
                                border-radius:30px;
                                border:6px solid #B0BEC5;
                            '''
            )
            i.setEnabled(True)
        self.timer.stop()

    def ficha(self):
        print('Ficha')
        send = self.sender()
        ficha = int(send.objectName()[8:])-1
        send.setStyleSheet(
            f'''
                                        image: url({self.imagenes[f'{self.lista[ficha] % 6}']});
                                        color: rgb(255, 255, 255);
                                        border-radius:30px;
                                        border-radius:30px;
                                        border:6px solid #B0BEC5;
                                    '''
        )
        if self.presionados[0] == -1:
            self.presionados[0] = ficha
            send.setEnabled(False)

        elif self.presionados[0]!=-1 and self.lista[self.presionados[0]]%6 == self.lista[ficha]%6:
            send.setEnabled(False)
            self.partida['fichas']+=1
            self.presionados = [-1,-1]
        else:
            self.partida['intentos']+=1
            self.presionados[1] = ficha
            for i in self.botones:
                i.clicked.disconnect(self.ficha)
                i.clicked.connect(self.espera)
            self.v_time.start(2000)

        if self.partida['fichas'] == 6:
            self.msj('Felicidades, haz ganado.')
            self.btn_Si.show()
            self.btn_No.show()
            self.lbl_Pregunta.show()
            self.lbl_o.show()
            self.btn_No.setEnabled(True)
            self.btn_Si.setEnabled(True)

    def mix(self):
        lista = [i for i in range(12)]
        for i in range(12):
            numero = random.randint(1,12) - 1
            lista[numero],lista [i] =lista [i],lista [numero]
        return lista

    #Area de los Slots
    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

    def si(self):
        self.partida['fichas'] = 0
        for i in self.botones:
            i.setStyleSheet(
                '''
                                image: url(:/Ejercicios/EquisG_1.png);
                                color: rgb(255, 255, 255);
                                border-radius:30px;
                                border-radius:30px;
                                border:6px solid #B0BEC5;
                            '''
            )
            i.setEnabled(True)
        self.jugar()
        self.btn_Si.hide()
        self.btn_No.hide()
        self.lbl_Pregunta.hide()
        self.lbl_o.hide()
        self.btn_No.setEnabled(False)
        self.btn_Si.setEnabled(False)


    def no(self):
        mensaje = f'Ya finalizó el juego \nPartidas jugadas: {self.partida['juegos']}\nErrores: {self.partida['intentos']}'
        self.msj(mensaje)
        self.btn_No.setEnabled(False)
        self.btn_Si.setEnabled(False)
        for i in self.botones:
            i.setEnabled(False)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())