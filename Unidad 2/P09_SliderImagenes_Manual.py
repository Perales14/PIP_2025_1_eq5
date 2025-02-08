import sys
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "P09_SliderImagenes_Manual.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#Comando para crear el Recursos_rc.py, desde "archivos" y lo cree en esta carpeta, no alla
# pyrcc5 .\Recursos.qrc -o '..\Unidad 2\Recursos_rc.py'
# como tal el codigo es
#asi lo creara en la carpeta en la que se encuentre
# pyrcc5 .\Recursos.qrc -o Recursos_rc.py

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Selector_imagen.setMinimum(1)
        self.Selector_imagen.setMaximum(3)
        self.Selector_imagen.setSingleStep(1)
        self.Selector_imagen.setValue(1)
        self.Selector_imagen.valueChanged.connect(self.cambiarValor)
        self.diccionarioDatos ={
            0: (":/Images/Gatos.png",["Gato", "4 meses", "Raton"]),
            1: (":/Logos/FIT_logo_vertical.png", ["Castor","65 años", "Estudiar"]),
            2: (":/Logos/log_uat_nuevo.png", ["Correcaminos", "75 años", "Superacion"]),
        }
        self.indice = 0
        self.ObtenerDatos()

    def ObtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        Juguete = self.diccionarioDatos[self.indice][1][2]
        # print(nombre)
        print("Nombre: ", nombre)

        self.txt_Nombre.setText(nombre)
        print("Edad: ", nombre)
        self.txt_Edad.setText(str(edad))
        print("Edad: ", edad)
        self.txt_Juguete.setText(Juguete)
        print("asadas")


    def cambiarValor(self):
        print("cambiar valor")
        self.indice = (self.indice + 1) % 3
        self.indice = self.Selector_imagen.value()
        print("Valor cambiado")
        self.obtenerDatos()
        print('A')
        self.Imagen_descripcion.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))
        print(self.diccionarioDatos[self.indice][0])


#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())