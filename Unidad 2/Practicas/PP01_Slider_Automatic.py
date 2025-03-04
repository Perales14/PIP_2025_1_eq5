import sys
from PyQt5 import uic, QtWidgets,QtGui, QtCore
qtCreatorFile = "PP01_Slider_Automatic.ui" # Nombre del archivo aqui
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
        self.Selector_imagen.setMinimum(1)
        self.Selector_imagen.setMaximum(9)
        self.Selector_imagen.setSingleStep(1)
        self.Selector_imagen.setValue(1)
        self.Selector_imagen.valueChanged.connect(self.cambiarValor)
        # self.Selector_imagen.valueChanged.connect(self.cambiarValor)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)
        self.segundoPlano.start(1000)
        self.Segundos = 4

        self.diccionarioDatos ={
            0: (":/Ejercicios/Archivos/Adobe Express - file (1).png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            1: (":/Ejercicios/Archivos/export202502092116429107.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            2: (":/Ejercicios/Archivos/export202502092135328918.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            3: (":/Ejercicios/Archivos/export202502092201258300.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            4: (":/Ejercicios/Archivos/export202502092210045727.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            5: (":/Ejercicios/Archivos/export202502092217592371.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            6: (":/Ejercicios/Archivos/export202502092224352078.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            7: (":/Ejercicios/Archivos/export202502092235269890.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            8: (":/Ejercicios/Archivos/export202502092244329519.png", ["Etiqueta1", "Etiqueta2", "Etiqueta3"]),
            9: (":/Ejercicios/Archivos/export202502092342196874.png", ["Etiqueta1", "Etiqueta2","Etiqueta3"])
        }
        self.indice = 0
        [':/Ejercicios/Archivos/Adobe Express - file (1).png', ]
        self.ObtenerDatos()

    def controlSegundoPlano(self):
        self.Segundos -= 1

        print("Segundos del Timer: ", self.Segundos)

        if self.Segundos == -1:
            self.segundoPlano.stop()
            self.Segundos = 4
            self.segundoPlano.start(1000)
            self.cambiarValor()
            self.Selector_imagen.setValue(self.indice)



    def temporizar2doPlano(self):
        self.segundoPlano.start(3000)

    def ObtenerDatos(self):
        # print("Obtener Datos")
            try:
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
            except Exception as e:
                print("Error: ", e)


    def cambiarValor(self):
        try:
            print("cambiar valor")
            self.indice = (self.indice + 1) % 9
            # self.indice = self.Selector_imagen.value()
            print("Valor cambiado")
            self.ObtenerDatos()
            print('A')
            self.Imagen_descripcion.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))
            print(self.diccionarioDatos[self.indice][0])
        except Exception as e:
            print("Errossr: ", e)


#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())