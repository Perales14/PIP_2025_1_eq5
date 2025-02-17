import sys
import random as rand
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "U2_E16_OperacionesAritmeticas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_Temporizador.clicked.connect(self.temporizar2doPlano)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)

        self.temporizadorOperaciones = QtCore.QTimer()
        self.temporizadorOperaciones.timeout.connect(self.actualizarOperacion)

        self.resultado = 0
        self.segundos = -1
        self.puntaje = 0
        self.opcion = rand.randint(0, 3)
        self.opcionBoton = rand.randint(0, 2)
        self.numeroAleatorio1 = rand.randint(0, 20)
        self.numeroAleatorio2 = rand.randint(1, 20)

        self.btn_1.clicked.connect(self.verificarRespuesta)
        self.btn_2.clicked.connect(self.verificarRespuesta)
        self.btn_3.clicked.connect(self.verificarRespuesta)

        self.txt_Segundos.textChanged.connect(self.CheckLetterS)

    def verificarRespuesta(self):
        boton = self.sender()  # Obtener el botón que se presionó
        if boton.text() == str(self.resultado):
            self.puntaje += 1
            print(f"Puntaje: {self.puntaje}")
        # No hacer nada si la respuesta es incorrecta

    #Área de los Slots
    def actualizarOperacion(self):
        # Generar nuevos valores aleatorios
        self.opcion = rand.randint(0, 3)
        self.opcionBoton = rand.randint(0, 2)
        self.numeroAleatorio1 = rand.randint(0, 20)
        self.numeroAleatorio2 = rand.randint(1, 20)

        # Actualizar la operación y los botones
        self.mostrarOperacionesActualizadas()

    def mostrarOperacionesActualizadas(self):
        if self.opcion == 0:
            self.resultado = self.numeroAleatorio1 + self.numeroAleatorio2
            self.lbl_OperArit.setText(f'Operación Aritmética: {str(self.numeroAleatorio1)}'
                                      f' + {str(self.numeroAleatorio2)} = ?')
        elif self.opcion == 1:
            self.resultado = self.numeroAleatorio1 - self.numeroAleatorio2
            self.lbl_OperArit.setText(f'Operación Aritmética: {str(self.numeroAleatorio1)}'
                                      f' - {str(self.numeroAleatorio2)} = ?')
        elif self.opcion == 2:
            self.resultado = self.numeroAleatorio1 * self.numeroAleatorio2
            self.lbl_OperArit.setText(f'Operación Aritmética: {str(self.numeroAleatorio1)}'
                                      f' * {str(self.numeroAleatorio2)} = ?')
        elif self.opcion == 3:
            self.resultado = round(self.numeroAleatorio1 / self.numeroAleatorio2, 2)
            self.lbl_OperArit.setText(f'Operación Aritmética: {str(self.numeroAleatorio1)}'
                                      f' / {str(self.numeroAleatorio2)} = ?')

            # Asignar el resultado correcto a un botón aleatorio
        botones = [self.btn_1, self.btn_2, self.btn_3]
        for i, boton in enumerate(botones):
            if i == self.opcionBoton:
                boton.setText(str(self.resultado))
            else:
                boton.setText(str(rand.randint(0, 100)))

    def controlSegundoPlano(self):
        self.txt_Segundos.setText(str(self.segundos))
        self.segundos -= 1

        if self.segundos == -1:
            self.segundoPlano.stop()
            self.temporizadorOperaciones.stop()
            self.btn_1.setEnabled(False)
            self.btn_2.setEnabled(False)
            self.btn_3.setEnabled(False)
        pass

    def temporizar2doPlano(self):
        self.segundos = int(self.txt_Segundos.text())
        self.segundoPlano.start(1000)
        self.temporizadorOperaciones.start(5000)
        self.mostrarOperacionesActualizadas()

    def CheckLetterS(self):
        segundos = self.txt_Segundos.text()
        try:
            float(segundos)
            segundos = "".join(segundos.split())
            self.txt_Segundos.setText(segundos)

        except:
            QtWidgets.QToolTip.showText(self.txt_Segundos.mapToGlobal(self.txt_Segundos.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Segundos.setFocus()
            segundos = segundos[:-1]
            self.txt_Segundos.setText(segundos)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())