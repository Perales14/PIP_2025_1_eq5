import sys #Este programa me hace falta implementar
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "U2_E11_RelojAlarma.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.horasRestantes = 0
        self.minutosRestantes = 0
        self.segundosRestantes = 60

        self.horaActual = 0
        self.minutoActual = 0

        self.horaAlarma = 0
        self.minutoAlarma = 0

        self.btn_Guardar.clicked.connect(self.obtenerHoraActual)
        self.btn_AgrAlarma.clicked.connect(self.controlAlarmaSegundoPlano)

        self.alarmaSegundoPlano = QtCore.QTimer()
        self.alarmaSegundoPlano.timeout.connect(self.tiempoRestanteSegundoPlano)

        self.txt_Horas_Act.textChanged.connect(self.CheckLetterHrAct)
        self.txt_Minutos_Act.textChanged.connect(self.CheckLetterMinAct)
        self.txt_Horas_Alar.textChanged.connect(self.CheckLetterHrAlrm)
        self.txt_Minutos_Alar.textChanged.connect(self.CheckLetterMinAlrm)

    #Área de los Slots

    def obtenerHoraActual(self):
        self.horaActual = int(self.txt_Horas_Act.text())
        self.minutoActual = int(self.txt_Minutos_Act.text())

    def obtenerAlarma(self):
        self.horaAlarma = int(self.txt_Horas_Alar.text())
        self.minutoAlarma = int(self.txt_Minutos_Alar.text())

        self.horasRestantes = self.horaAlarma - self.horaActual
        self.minutosRestantes = self.minutoAlarma - self.minutoActual

        if self.minutosRestantes < 0:
            self.minutosRestantes += 60
            self.horasRestantes -= 1

        if self.horasRestantes < 0:
            self.horasRestantes += 24

        self.segundosRestantes = 0

    def tiempoRestanteSegundoPlano(self):

        self.segundosRestantes -= 1

        if self.segundosRestantes < 0:
            self.segundosRestantes = 59
            self.minutosRestantes -= 1

        if self.minutosRestantes < 0:
            self.minutosRestantes = 59
            self.horasRestantes -= 1

        if self.horasRestantes < 0:
            self.horasRestantes = 0
            self.minutosRestantes = 0
            self.segundosRestantes = 0
            self.alarmaSegundoPlano.stop()
            QtWidgets.QMessageBox.information(self, "Alarma", "¡Es hora!")
            return

        tiempo = (f'La Alarma sonará en: {self.horasRestantes} horas {self.minutosRestantes} minutos con '
                  f'{self.segundosRestantes} segundos') #Se imprime el tiempo restante

        self.lbl_Horas.setText(str(self.horasRestantes))
        self.lbl_Minutos.setText(str(self.minutosRestantes))
        self.lbl_Segundos.setText(str(self.segundosRestantes))

        print(tiempo)

    def controlAlarmaSegundoPlano(self):
        self.obtenerAlarma()
        self.alarmaSegundoPlano.start(1000)

    def CheckLetterHrAct(self):
        horaActual = self.txt_Horas_Act.text()
        try:
            float(horaActual)
            horaActual = "".join(horaActual.split())
            self.txt_Horas_Act.setText(horaActual)

        except:
            QtWidgets.QToolTip.showText(self.txt_Horas_Act.mapToGlobal(self.txt_Horas_Act.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Horas_Act.setFocus()
            horaActual = horaActual[:-1]
            self.txt_Horas_Act.setText(horaActual)

    def CheckLetterMinAct(self):
        minutoActual = self.txt_Minutos_Act.text()
        try:
            float(minutoActual)
            minutoActual = "".join(minutoActual.split())
            self.txt_Minutos_Act.setText(minutoActual)

        except:
            QtWidgets.QToolTip.showText(self.txt_Minutos_Act.mapToGlobal(self.txt_Minutos_Act.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Minutos_Act.setFocus()
            minutoActual = minutoActual[:-1]
            self.txt_Minutos_Act.setText(minutoActual)
    
    def CheckLetterHrAlrm(self):
        horaAlarma = self.txt_Horas_Alar.text()
        try:
            float(horaAlarma)
            horaAlarma = "".join(horaAlarma.split())
            self.txt_Horas_Alar.setText(horaAlarma)

        except:
            QtWidgets.QToolTip.showText(self.txt_Horas_Alar.mapToGlobal(self.txt_Horas_Alar.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Horas_Alar.setFocus()
            horaAlarma = horaAlarma[:-1]
            self.txt_Horas_Alar.setText(horaAlarma)
            
    def CheckLetterMinAlrm(self):
        minutoAlarma = self.txt_Minutos_Alar.text()
        try:
            float(minutoAlarma)
            minutoAlarma = "".join(minutoAlarma.split())
            self.txt_Minutos_Alar.setText(minutoAlarma)

        except:
            QtWidgets.QToolTip.showText(self.txt_Minutos_Alar.mapToGlobal(self.txt_Minutos_Alar.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Minutos_Alar.setFocus()
            minutoAlarma = minutoAlarma[:-1]
            self.txt_Minutos_Alar.setText(minutoAlarma)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())