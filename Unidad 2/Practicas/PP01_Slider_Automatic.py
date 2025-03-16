import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "PP01_Slider_Automaticv.ui"  # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Selector_imagen.setMinimum(1)
        self.Selector_imagen.setMaximum(9)
        self.Selector_imagen.setSingleStep(1)
        self.Selector_imagen.setValue(1)
        self.Selector_imagen.valueChanged.connect(self.cambiarValor)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)
        self.segundoPlano.start(1000)
        self.Segundos = 3
        self.diccionarioDatos = {
            1: (":/Ejercicios/Archivos/Adobe Express - file (1).png", ["Michi"]),
            2: (":/Ejercicios/Archivos/export202502092116429107.png", ["Pelusa"]),
            3: (":/Ejercicios/Archivos/export202502092135328918.png", ["Garfiel"]),
            4: (":/Ejercicios/Archivos/export202502092201258300.png", ["Bigotes"]),
            5: (":/Ejercicios/Archivos/export202502092210045727.png", ["Nieve"]),
            6: (":/Ejercicios/Archivos/export202502092217592371.png", ["Salem"]),
            7: (":/Ejercicios/Archivos/export202502092224352078.png", ["Felix"]),
            8: (":/Ejercicios/Archivos/export202502092235269890.png", ["Minino"]),
            9: (":/Ejercicios/Archivos/export202502092244329519.png", ["Simba"]),
        }

        self.indice = 1
        self.actualizarDatos()

    def controlSegundoPlano(self):
        self.Segundos -= 1
        if self.Segundos == -1:
            self.Segundos = 3
            self.indice = self.indice + 1 if self.indice < 9 else 1
            self.Selector_imagen.blockSignals(True)
            self.Selector_imagen.setValue(self.indice)
            self.Selector_imagen.blockSignals(False)
            self.actualizarDatos()

    def actualizarDatos(self):
        try:
            nombre = self.diccionarioDatos[self.indice][1][0]
            self.txt_Nombre.setText(nombre)
            self.Imagen_descripcion.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))
        except Exception as e:
            print("Error al actualizar datos:", e)

    def cambiarValor(self):
        try:
            nuevo_valor = self.Selector_imagen.value()
            if nuevo_valor != self.indice:  # Evitar doble actualización
                self.indice = nuevo_valor
                self.actualizarDatos()
        except Exception as e:
            print("Error en cambiarValor:", e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
