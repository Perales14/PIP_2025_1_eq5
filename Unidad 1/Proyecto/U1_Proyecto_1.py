import sys
from tkinter.constants import ROUND

from PyQt5 import uic, QtWidgets, QtCore
from matplotlib.rcsetup import validate_int_or_None

qtCreatorFile = "U1_Proyecto_1.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        # bontes (btn_Cargar, btn_Eliminar, btn_Guardar,btn_Modificar)
        self.txt_Valores.setEnabled(False)
        self.btn_Cargar.clicked.connect(self.cargar)
        self.btn_Eliminar.clicked.connect(self.eliminar)
        self.btn_Guardar.clicked.connect(self.guardar)
        self.btn_Modificar.clicked.connect(self.modificar)
        self.btn_Save.clicked.connect(self.save)
        # self.save.clicked.connect(self.save)

        self.lista = []
        self.txt_Valor.textChanged.connect(self.CheckLetter)
        self.txt_Modifica.textChanged.connect(self.CheckLetter)
        self.txt_Elimina.textChanged.connect(self.CheckLetter)



    def cargar(self):
        #buscar archivo llamado "datos.txt" y cargar los datos
        try:
            archivo = open("datos.txt","r")
            datos = archivo.read()
            archivo.close()
        except Exception as e:
            self.msj("No se encontró el archivo datos.txt")
            print(e)
            return
        datos = datos.split(",")
        t = len(datos)
        if datos[t-1] == "":
            datos.pop(t-1)

        try:
            self.lista = [float(i) for i in datos]
        except Exception as e:
            self.msj("El archivo datos.txt no tiene el formato correcto")
            print(e)
            return
        self.txt_Valores.setText(". ".join([str(i) for i in self.lista]))
        self.btn_Cargar.setEnabled(False)

        self.changeStyleSheet(self.btn_Cargar)
        self.calcular()


    def eliminar(self):
        valor = self.txt_Elimina.text()
        if valor == "":
            self.msj("Por favor, ingrese un valor a eliminar")
            return
        try:
            valor = float(valor)
        except Exception as e:
            self.msj("Solo se permiten números")
            self.clearTxt(self.txt_Elimina)
            print(e)
            return
        try:
            posicion = self.lista.index(valor)
        except Exception as e:
            self.msj("El valor no se encuentra en la lista")
            self.clearTxt(self.txt_Elimina)
            return
        self.lista.pop(posicion)
        self.txt_Valores.setText(", ".join([str(i) for i in self.lista]))
        self.clearTxt(self.txt_Elimina)
        self.calcular()


    def guardar(self):
        valor = self.txt_Valor.text()
        if valor == "":
            self.msj("Por favor, ingrese un valor")
            return

        try:
            valor = float(valor)
            self.addrefresh(round(valor,2))
            self.clearTxt(self.txt_Valor)
        except Exception as e:
            self.msj("Solo se permiten números")
            self.clearTxt(self.txt_Valor)
            print(e)

        self.calcular()



    def modificar(self):
        valor = self.txt_Modifica.text()
        if valor == "":
            self.msj("Por favor, ingrese un valor a modificar")
            return
        try:
            valor = float(valor)
        except Exception as e:
            self.msj("Solo se permiten números")
            self.txt_Modifica.setText("")
            print(e)
            return
        try:
            posicion = self.lista.index(valor)
        except Exception as e:
            self.msj("El valor no se encuentra en la lista")
            self.txt_Modifica.setText("")
            return
        self.msj("A continuación, ingrese el nuevo valor")
        self.entrada = QtWidgets.QInputDialog()#.changeEvent(QtCore.QEvent.Type(1))
        self.entrada.setStyleSheet("""
        QLineEdit {
            font: 20pt "Forte";
            color: rgb(0, 0, 0);
            border-radius: 35px;
            border: 10px solid rgb(33, 150, 243);   
        }
        """)
        # self.entrada.textValueChanged.connect(self.chechprint)
        valor = self.entrada.getText(self.entrada, "Nuevo valor", "Ingrese el nuevo valor")#, QtWidgets.QLineEdit.NoEcho, "Aaa")
        # valor = [1,1]

        if valor[1]:
            try:
                valor = float(valor[0])
                print(valor)
            except Exception as e:

                self.msj("Solo se permiten números")
                self.txt_Modifica.setText("")
                print(e)
                return

            self.lista.pop(posicion)
            self.addrefresh(round(valor,2))
            self.clearTxt(self.txt_Modifica)
        self.calcular()

    def save(self):
        #verificar si el archivo ya existe, en caso de existir preguntar si se desea sobreescribir
        #si se desea sobreescribir, guardar los datos en el archivo
        #si no, no hacer nada
        if len(self.lista) == 0:
            self.msj("No hay valores en la lista")
            return

        try:
            archivo = open("datos.txt")
            archivo.close()
            #si no rompe, el archivo existe, por lo que se le pregunta si sobre escribir o que de otro nombre para el archivo
            respuesta = QtWidgets.QMessageBox.question(None, "Sobreescribir", "¿Desea sobreescribir el archivo?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            if respuesta == QtWidgets.QMessageBox.No:
                nombre = QtWidgets.QInputDialog.getText(None, "Nombre del archivo", "Ingrese el nombre del archivo")
                if nombre[1]:
                    #el "nombre[1]" se refiere a la seleccion que hizo, si es verdad pues dio "ok" o siguiente, lo que haya, si es falso, pues presiono
                    # que no, o cerro, y esa respesta no nos sirve, por eso no hay else
                    archivo = open(nombre[0]+".txt", "w")
                    archivo.write(", ".join([str(i) for i in self.lista]))
                    archivo.close()
                return

            else:
                archivo = open("datos.txt", "w")
                archivo.write(", ".join([str(i) for i in self.lista]))
                archivo.close()
        except:
            archivo = open("datos.txt","w")
            archivo.write(", ".join([str(i) for i in self.lista]))
            archivo.close()


    def calcular(self):
        #metodo para calcular valor menor, valor mayor, desviacion estandar, Media, Mediana, Moda y Varianza
        #nombré de lables = lbl_VMa, lbl_VMe, lbl_Media_2, lbl_Mediana_2, lbl_Moda_2, lbl_Varianza_2, lbl_DE
        t = len(self.lista)
        mayor = round(self.lista[t-1],2) #if t>0 else round(self.lista[0],2)
        menor = round(self.lista[0],2)
        suma = 0
        suma += sum(self.lista)
        media = round(suma/t,2)

        if t%2 == 0:
            mediana = self.lista[int(t/2)] + self.lista[int(t/2)-1]
            mediana = mediana/2
        else:
            mediana = self.lista[int(t/2)]
        mediana = round(mediana,2)

        moda = self.lista[0]
        veces = self.lista.count(moda)
        for i in self.lista:
            if self.lista.count(i)>veces:
                moda = i
                veces = self.lista.count(i)
        moda = round(moda,2)
        sumatoria = 0
        for i in self.lista:
            sumatoria += (i-media)**2
        if t == 1:
            varianza = 0
            desviacion = 0
        else:
            varianza = sumatoria/(t-1) #DIVISION ENTRE 0 .-.
            desviacion = round(varianza**0.5,2)
            varianza = round(varianza,2) #asi, para que el cálculo de la desviación sea lo más correcto

        self.lbl_VMa.setText(str(mayor))
        self.lbl_VMe.setText(str(menor))
        self.lbl_Media_2.setText(str(media))
        self.lbl_Mediana_2.setText(str(mediana))
        self.lbl_Moda_2.setText(str(moda))
        # self.lbl_Varianza_2.setText(str(varianza))
        self.lbl_DE.setText(str(desviacion))



        # if len(self.lista) == 0:
        #     self.msj("No hay valores en la lista")
        #     return
        # menor = self.lista[0]
        # mayor = self.lista[len(self.lista)-1]
        # suma = 0
        # for i in self.lista:
        #     suma += i
        # media = suma/len(self.lista)
        # if len(self.lista)%2 == 0:
        #     mediana = (self.lista[int(len(self.lista)/2)] + self.lista[int(len(self.lista)/2)-1])/2
        # else:
        #     mediana = self.lista[int(len(self.lista)/2)]
        # moda = self.lista[0]
        # rep = 0
        # for i in self.lista:
        #     if self.lista.count(i)>rep:
        #         moda = i
        #         rep = self.lista.count(i)
        # varianza = 0
        # for i in self.lista:
        #     varianza += (i-media)**2
        # varianza = varianza/len(self.lista)
        # desviacion = varianza**0.5

        pass

    def addrefresh(self, valor):
        self.add_n(valor)
        self.txt_Valores.setText(", ".join([str(i) for i in self.lista]))

    def add_n(self, valor):
        #agrega un valor a la lista, en orden
        t = len(self.lista)
        if t==0:
            self.lista.append(valor)
            self.btn_Cargar.setEnabled(False)
            self.changeStyleSheet(self.btn_Cargar)
            return
        for i in range(t):
            if valor< self.lista[i]:
                self.lista.insert(i,valor)
                return

        self.lista.append(valor)

    def changeStyleSheet(self, label):
        label.setStyleSheet("""
           QPushButton:disabled {
                background-color: rgb(150, 150, 150);
                font: 20pt "Forte";
                color: rgb(200, 200, 200);
                border-radius: 35px;
                border: 10px solid rgb(120, 120, 120);
           }
           """)

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        # a = QtWidgets.QAbstractButtonQ
        m.setText(txt)
        m.exec_()

    def clearTxt(self, txt):
        txt.setText("")
        txt.setFocus()

    def CheckLetter(self):
        #para que solo se permitan numeros
        enviador = self.sender() #Sender hace referencia al "objeto" que llamo el metodo, por lo que es como
        #pasar el objeto como parametro, pero sin hacerlo explicito, ya que cuando se hace, el metodo regresa nulo y no se puede
        # usar eso para parametro de un connect XD
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

    #Area de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())