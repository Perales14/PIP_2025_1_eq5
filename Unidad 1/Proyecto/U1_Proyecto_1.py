import sys
from PyQt5 import uic, QtWidgets
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
        self.btn_Cargar.clicked.connect(self.cargarr)
        self.btn_Eliminar.clicked.connect(self.eliminar)
        self.btn_Guardar.clicked.connect(self.guardar)
        self.btn_Modificar.clicked.connect(self.modificar)

    def cargarr(self):
        text, ok = QtWidgets.QInputDialog.getText(None, "Input Dialog", "Nombre del archivo")
        if ok:
            print(f"Nombre del archivo para guardar {text}")
        pass

    def cargar(self):
        #Leer el archivo desde la carpeta Archivo, con el nombre de datos.txt
        #     ruta = "../../Archivos/datos.txt"
        print("Cargar")
        try:
            ruta = "datos.txt"
            archivo = open(ruta, "r")
            datos = archivo.read()
            archivo.close()
            self.txt_Valores.setText(datos)
        except Exception as e:
            self.msj("Error al cargar el archivo: "+str(e))

    def eliminar(self):
        lista = self.txt_Valores.text().split(", ")
        valor = self.txt_Elimina.text()
        if valor == "":
            self.msj("Ingrese un valor a eliminar")
            return
        try:
            lista.remove(valor)
            self.txt_Valores.setText(", ".join(lista))
            archivo = open("datos.txt", "w")
            archivo.write(", ".join(lista))
        except Exception as e:
            self.msj("Error al eliminar el valor: ")


    def guardar(self):
        try:
            ruta = "datos.txt"
            #CONCATENAR al archivo el dato encontrado en txt-valor
            archivo = open(ruta, "a")
            dato = self.txt_Valor.text()
            if dato != "":
                archivo.write(dato+", ")
                archivo.close()
                self.txt_Valor.setText("")
                self.cargar()
            else:
                self.msj("Ingrese un valor para guardarlo")


        except Exception as e:
            self.msj("Error AL cargar el archivo: "+str(e))

    def modificar(self):
        pass

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        # a = QtWidgets.QAbstractButtonQ
        m.setText(txt)
        m.exec_()

    #Area de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())