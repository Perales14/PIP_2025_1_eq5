import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "U2_E17_Semáforo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_Simular_Semaforo.clicked.connect(self.cronometroSegundoPlanoSemaforos)

        self.segundoPlanoSemaforoVerde = QtCore.QTimer()
        self.segundoPlanoSemaforoVerde.timeout.connect(self.controlSegundoPlanoSemaforoVerde)

        self.segundoPlanoSemaforoAmarillo = QtCore.QTimer()
        self.segundoPlanoSemaforoAmarillo.timeout.connect(self.controlSegundoPlanoSemaforoAmarillo)

        self.segundoPlanoSemaforoRojo = QtCore.QTimer()
        self.segundoPlanoSemaforoRojo.timeout.connect(self.controlSegundoPlanoSemaforoRojo)

        self.luzVerde = 45
        self.luzAmarilla = 3
        self.luzRoja = 60

        self.diccionarioSemaforos = {
            1: ":/Ejercicios/Archivos/Verde.png",
            2: ":/Ejercicios/Archivos/Ambar_Amarillo.png",
            3: ":/Ejercicios/Archivos/Rojo.png"
        }

        self.indice = 0

    #Área de los Slots

    def controlSegundoPlanoSemaforoVerde(self):
        self.indice = 1

        self.lbl_imagenApagado.setPixmap(QtGui.QPixmap(
            self.diccionarioSemaforos[self.indice]))

        self.lbl_Tiempo_2.setText("Avance :D")
        self.lbl_Color.setText("El semáforo está en: Verde")
        self.lbl_Tiempo.setText(f"Espere: {str(self.luzVerde)}")

        self.luzVerde -= 1

        if self.luzVerde == 0:
            self.segundoPlanoSemaforoVerde.stop()
            self.segundoPlanoSemaforoAmarillo.start(1000)
        pass

    def controlSegundoPlanoSemaforoAmarillo(self):
        self.indice = 2

        self.lbl_imagenApagado.setPixmap(QtGui.QPixmap(
            self.diccionarioSemaforos[self.indice]))

        self.lbl_Tiempo_2.setText("Disminuya la velocidad ;)")
        self.lbl_Color.setText("El semáforo está en: Amarillo")
        self.lbl_Tiempo.setText(f"Espere: {str(self.luzAmarilla)}")

        self.luzAmarilla -= 1

        if self.luzAmarilla == 0:
            self.segundoPlanoSemaforoAmarillo.stop()
            self.segundoPlanoSemaforoRojo.start(1000)
        pass

    def controlSegundoPlanoSemaforoRojo(self):
        self.indice = 3

        self.lbl_imagenApagado.setPixmap(QtGui.QPixmap(
            self.diccionarioSemaforos[self.indice]))

        self.lbl_Tiempo_2.setText("No puede avanzar :(")
        self.lbl_Color.setText("El semáforo está en: Rojo")
        self.lbl_Tiempo.setText(f"Espere: {str(self.luzRoja)}")

        self.luzRoja -= 1

        if self.luzRoja == 0:
            self.segundoPlanoSemaforoRojo.stop()
            self.segundoPlanoSemaforoVerde.start(1000)
            self.luzVerde = 45
            self.luzAmarilla = 3
            self.luzRoja = 60
        pass

    def cronometroSegundoPlanoSemaforos(self):
        self.segundoPlanoSemaforoVerde.start(1000)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())