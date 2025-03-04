from PyQt5 import uic, QtWidgets, QtGui
import sys
import random
qtCreatorFile = "U2_E05_Parte2_Juego_del_Ahorcado.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Jugar.clicked.connect(self.jugar)
        # self.btn_Letra.clicked.connect(self.letra)
        self.letras = []
        # self.btn_Reiniciar.clicked.connect(self.reiniciar)
        # self.palabras = ['hola','mundo','python','java','casa','perro','gato','pajaro','elefante','computadora']
        #la lista de palabras pero en mayusculas
        self.palabra = ''
        self.palabras = [
        "manzana", "computadora", "python", "elefante", "biblioteca", "automovil", "programacion",
        "auriculares", "ventilador", "almohada", "cascada", "helicoptero", "mariposa", "astronauta",
        "camaleon", "murcielago", "escritorio", "refrigerador", "microfono", "pantalla", "carretera",
        "luciérnaga", "electricidad", "cementerio", "telescopio", "universo", "esqueleto", "cangrejo",
        "murmullo", "explorador", "escalera", "tornado", "jirafa", "travesura", "circuito", "catedral",
        "destello", "laberinto", "camioneta", "espantapajaros", "abrelatas", "zoologico", "montaña",
        "marinero", "caracol", "descubrimiento", "fotografia", "isla", "pirata", "globo", "magnetismo",
        "campeon", "universidad", "muralla", "piscina", "pradera", "reloj", "pluma", "bateria",
        "telefono", "hospital", "corazon", "oceano", "tiburon", "volcan", "guitarra", "martillo",
        "tijeras", "avion", "bosque", "ciudad", "tren", "rayo", "planeta", "galaxia", "cometa",
        "nube", "trueno", "relampago", "vampiro", "fantasma", "bruja", "robot", "dragón", "caballero",
        "espada", "escudo", "castillo", "reina", "rey", "princesa", "caballo", "caravana", "carpintero",
        "montaña", "añoranza", "señal", "bañera", "niñez", "año", "muñeca", "baño", "cañón", "sueño"
        ]
        self.botones = [self.btn_N_]
        self.botones[0].setObjectName("btn_Ñ")
        self.botones[0].clicked.connect(self.letra)

        for i in range(26):
            boton = self.findChild(QtWidgets.QPushButton, f"btn_{chr(65+i)}")
            #asi para obtener el "object" de los 26 botones para ponerles la misma funcion, la cual al tener un
            # sender, puede saber cual boton fue presionado
            boton.clicked.connect(self.letra)
            self.botones.append(boton)

        a = "btn_"+chr(65+i)


    def letra(self):
        if self.palabra == '':
            self.msj("Primero debes presionar el boton Jugar")
            return

        if self.intentos == 9:
            self.msj("Perdiste")
            return

        send = self.sender()
        letra = send.objectName()[-1].lower()
        # send.setEnabled(False)
        send.setStyleSheet("""
            font: 75 20pt "Script MT Bold";
            background-color: rgb(100, 0, 1);
            color: rgb(200, 200, 200);
            border-radius: 30px;
            border: 6px solid #90A4AE;
        """)

        if letra in self.letras:
            self.msj("Ya has usado esa letra")
            return
        print(letra)
        self.letras.append(letra)
        if letra in self.palabra:
            self.palabra_oculta = ''
            for l in self.palabra:
                if l in self.letras:
                    self.palabra_oculta += l
                else:
                    self.palabra_oculta += '_ '
            self.lbl_Palabra_3.setText(self.palabra_oculta)
            if '_' not in self.palabra_oculta:
                self.msj("Ganaste")
        else:
            print(self.palabra)
            self.intentos += 1
            self.lbl_imagenGatos_2.setPixmap(QtGui.QPixmap(":/Ejercicios/"+str(self.intentos)+".png"))
            if self.intentos == 9:
                self.msj("Perdiste")


    def jugar(self):
        self.palabra = random.choice(self.palabras)
        self.palabra_oculta = '_ '*len(self.palabra)
        self.lbl_Palabra_3.setText(self.palabra_oculta)
        self.intentos = 0
        for i in self.botones:
            i.setStyleSheet("""
                font: 75 20pt "Script MT Bold";
                background-color: rgb(130, 0, 2);
                color: rgb(255, 255, 255);
                border-radius:30px;
                border:6px solid #B0BEC5;
            """)
        self.lbl_imagenGatos_2.setPixmap(QtGui.QPixmap(":/Ejercicios/Base_Ahorcado.png"))
        # self.lbl_Imagen.setPixmap(QtGui.QPixmap(self.imagenes[self.intentos]))
        self.letras = []

    def reiniciar(self):
        self.jugar()
        self.txt_Letra.setText('')
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
