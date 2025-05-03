import sys
from PyQt5 import uic, QtWidgets, QtCore

import serial as tarjeta

qtCreatorFile = "PracticaX.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)
        self.bandera = 0
        self.datos = []

        self.btn_control.clicked.connect(self.control)
        self.btn_1.clicked.connect(self.control)
        self.btn_2.clicked.connect(self.control)
        self.btn_3.clicked.connect(self.control)


    def control(self):
        obj = self.sender()
        texto = obj.text()
        led = obj.objectName()[-1]
        if self.arduino is None:
            print("No hay conexion")
            return
        if self.arduino.isOpen():
            if texto == "PRENDER":
                obj.setText("APAGAR")
                c = led + "1"
                self.arduino.write(c.encode())
            elif texto == "APAGAR":
                obj.setText("PRENDER")
                c = led + "0"
                self.arduino.write(c.encode())

    def lecturas(self):
        try:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():
                    cadena = self.arduino.readline().decode().strip()
                    if cadena !="":
                        # print(cadena)
                        self.datos.append(cadena)
                        if self.bandera ==0:
                            print(cadena)
                            cadena = cadena.split("-")
                            # print('rompe')
                            cadena = cadena[:-1]
                            # cadena = str(cadena).split("-")
                            cadena = [int(i) for i in cadena]
                            print(cadena)
                            self.lista_datos1.addItem(str(cadena[0]))
                            self.lista_datos1.setCurrentRow(self.lista_datos1.count()-1)
                            self.lista_datos2.addItem(str(cadena[1]))
                            self.lista_datos2.setCurrentRow(self.lista_datos2.count() - 1)
                            self.lista_datos3.addItem(str(cadena[2]))
                            self.lista_datos3.setCurrentRow(self.lista_datos3.count() - 1)
        except Exception as e:
            print(e)

    def accion(self):
        texto = self.btn_accion.text()
        com = self.txt_com.text()
        if texto == "CONECTAR":
            self.arduino = tarjeta.Serial(com,baudrate=9600,timeout=1)
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
        elif texto == "DESCONECTAR":
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
        elif texto == "RECONECTAR":
            self.arduino.open()
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")


#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

#hacer los otros de los ejercicios,
# hacer comentarios en los ejercicios
# poner la conclusion de lo aprendido, sobre comportamientos y eso.
# cual consideramos que es la mejor para X o Y cosa