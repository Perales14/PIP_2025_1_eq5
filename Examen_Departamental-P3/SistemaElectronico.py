import sys
from PyQt5 import uic, QtWidgets
import serial
from PyQt5.QtCore import QTimer

qtCreatorFile = "Diseño_examen.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.arduino = serial.Serial("COM10", baudrate=9600, timeout=1)

        self.foco_habilitado = False
        self.motor_habilitado = False

        self.LH.clicked.connect(self.control)
        self.TH.clicked.connect(self.control)

        #timer de 1segundo, para leer y enviar datosc
        self.timer = QTimer()
        self.timer.timeout.connect(self.ciclo)
        self.timer.start(1000)

    def control(self):
        sender = self.sender()
        if sender.objectName() == "LH":
            self.foco_habilitado = not self.foco_habilitado
            self.LH.setText("Deshabilitar" if self.foco_habilitado else "Habilitar")
        elif sender.objectName() == "TH":
            self.motor_habilitado = not self.motor_habilitado
            self.TH.setText("Deshabilitar" if self.motor_habilitado else "Habilitar")

    def ciclo(self):

        foco_valor = 1 if self.foco_habilitado else 0
        motor_valor = 1 if self.motor_habilitado else 0

        mensaje = f"L:{foco_valor},T:{motor_valor}\n"
        print("mensaje", mensaje)
        self.arduino.write(mensaje.encode())

        # leer del arduino
        if self.arduino.inWaiting():
            linea = self.arduino.readline().decode().strip()
            if linea:
                try:
                    temp, ldr = linea.split(",")
                    #// conversion a % del ldr
                    ldr_val = int(ldr)
                    ldr_porcentaje = int((ldr_val / 1023) * 100)
                    self.lcd_number.display(float(temp))
                    self.progress_bar.setValue(ldr_porcentaje)
                except Exception as e:
                    print(f"Error al procesar datos: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
