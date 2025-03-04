import sys
import random
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "U2_E01_Parte2_Piedra_Papel_o_Tijera.ui" # Nombre del archivo aqui
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
        #boton jugar, boton piedra, boton papel, boton tijera
        self.eleccion =''
        self.btn_Jugar.clicked.connect(self.jugar)
        self.btn_Piedra.clicked.connect(self.selector)
        self.btn_Papel.clicked.connect(self.selector)
        self.btn_Tijera.clicked.connect(self.selector)

    def jugar(self):
        Eleccion = ['piedra','papel','tijera']
        eleccion_pc = random.choice(Eleccion)
        Ganador =''
        if self.eleccion == eleccion_pc:
            # self.msj("Empate")
            Ganador = "Empate"
        elif self.eleccion == 'piedra' and eleccion_pc == 'papel':
            # self.msj("Perdiste")
            Ganador = 'PC'
        elif self.eleccion == 'piedra' and eleccion_pc == 'tijera':
            # self.msj("Ganaste")
            Ganador = 'Jugador'
        elif self.eleccion == 'papel' and eleccion_pc == 'piedra':
            # self.msj("Ganaste")
            Ganador = 'Jugador'
        elif self.eleccion == 'papel' and eleccion_pc == 'tijera':
            # self.msj("Perdiste")
            Ganador = 'PC'
        elif self.eleccion == 'tijera' and eleccion_pc == 'piedra':
            # self.msj("Perdiste")
            Ganador = 'PC'
        elif self.eleccion == 'tijera' and eleccion_pc == 'papel':
            # self.msj("Ganaste")
            Ganador = 'Jugador'
        else:
            self.msj("Error, Debes elegir una opcion")
            return

        nombre = self.txt_Nombre.text()
        # lbl_imagenPapel_2 para mostrar la imagen de la pc
        if nombre == '':
            self.msj("Debes ingresar un nombre")
            return
        self.lbl_Escoge.setText("La Computadora Escogio: "+eleccion_pc)
        if eleccion_pc == 'piedra':
            self.lbl_imagenPapel_2.setPixmap(QtGui.QPixmap(":/Ejercicios/Archivos/export202502092342196874.png"))
        elif eleccion_pc == 'papel':
            self.lbl_imagenPapel_2.setPixmap(QtGui.QPixmap(":/Ejercicios/Archivos/export202502092342481393.png"))
        elif eleccion_pc == 'tijera':
            self.lbl_imagenPapel_2.setPixmap(QtGui.QPixmap(":/Ejercicios/Archivos/export202502092342556504.png"))

        if Ganador == 'Jugador':
            self.lbl_Escoge_2.setText("Ganador: "+nombre)
            self.lbl_Escoge_3.setText("Perdedor: PC")
        elif Ganador == 'PC':
            self.lbl_Escoge_2.setText("Ganador: PC")
            self.lbl_Escoge_3.setText("Perdedor: "+nombre)
        else:
            self.lbl_Escoge_2.setText("Ganador: Empate")
            self.lbl_Escoge_3.setText("Ganador: Empate")


    def eligeGanador(self,opA,opB):
        if opA == opB:
            return "D"
        if opA == 'piedra' or opB == 'piedra':

            if opA == 'papel' or opB == 'papel':
                #retorna T,F por que gana opA y pierde opB
                return True,False if opA == 'papel' else False,True

            elif opA == 'tijera' or opB == 'tijera':
                return True,False if opA == 'piedra' else False,True

        return True,False if opA == 'tijera' else False,True

        # if opA == 'papel' or opB == 'papel':
        #     if opA == 'tijera' or opB == 'tijera':
        #         return True,False if opA == 'tijera' else False,True
        # elif opA == 'piedra' and opB == 'piedra':
        #     return "D"

        # elif opA == 'piedra' and opB == 'papel':
        #     return False,True
        # elif opA == 'piedra' and opB == 'tijera':
        #     return True,False
        # elif opA == 'papel' and opB == 'piedra':
        #     return True,False
        # elif opA == 'papel' and opB == 'tijera':
        #     return False,True
        # elif opA == 'tijera' and opB == 'piedra':
        #     return False,True






# Area de los Signals
#     def impr(self):
#         print("Hola")
#         self.label.setText("Hola")
#         self.changeStyleSheet(self.label)
#
#         # self.changeStyleSheet(self.label)
#         time.sleep(2)
#         self.label.setText("Adios")
#         self.label.setStyleSheet("""
#             QLabel {
#                 background-color: rgb(0, 0, 255);
#                 color: white;
#                 font: bold 14px;
#                 border-radius: 10px;
#                 padding: 10px;
#             }
#         """)

    #
    # def changeStyleSheet(self, label):
    #     # cambia el stylesheet de un label
    #     label.setStyleSheet("""
    #        QLabel {
    #             text-decoration: underline;
    #             font: 20pt "Forte";
    #             color:rgb(0, 0, 0);
    #        }
    #        """)

    def selector(self):
        send = self.sender()
        if send == self.btn_Piedra:
            self.eleccion = 'piedra'
        elif send == self.btn_Papel:
            self.eleccion = 'papel'
        elif send == self.btn_Tijera:
            self.eleccion = 'tijera'
        else:
            print("Error")
        print('El jugador eligio:',self.eleccion)

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)

        m.exec_()

# def eligeGanador(opA,opB):
#     if opA == opB:
#         return "D", "D"
#     if opA == 'piedra' or opB == 'piedra':
#
#         if opA == 'papel' or opB == 'papel':
#             #retorna T,F por que gana opA y pierde opB
#             # print("piedra papel")
#             return [True,False] if opA == 'papel' else [False,True]
#
#         elif opA == 'tijera' or opB == 'tijera':
#             # print("piedra tijera")
#             return [True,False] if opA == 'piedra' else [False,True]
#     # print("tijera papel")
#     return [True,False] if opA == 'tijera' else [False,True]

#Area de los Slots
if __name__ == "__main__":
    # v = eligeGanador('piedra','papel')
    # print('piedra papel')
    # # print(v[0])
    # # print(v[1])
    # print(v)
    # lista =     ['piedra','papel','tijera']
    # #probar cada combinacion
    # for i in lista:
    #     for j in lista:
    #         print(f"{i} vs {j}")
    #         v = eligeGanador(i,j)
    #         # print(v[0])
    #         # print(v[1])
    #         print(v)
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
