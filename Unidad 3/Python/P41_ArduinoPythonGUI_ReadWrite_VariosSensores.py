import sys
from PyQt5 import uic, QtWidgets, QtCore

import serial as tarjeta

qtCreatorFile = "P41_ArduinoPythonGUI_ReadWrite_VariosSensores.ui" # Nombre del archivo aqui
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

    def control(self):
        texto = self.btn_control.text()
        if self.arduino is None:
            print("No hay conexion")
            return
        if self.arduino.isOpen():
            if texto == "PRENDER":
                self.btn_control.setText("APAGAR")
                self.arduino.write("1".encode())
            elif texto == "APAGAR":
                self.btn_control.setText("PRENDER")
                self.arduino.write("0".encode())

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
                            self.lista_datos.addItem(str(cadena))
                            self.lista_datos.setCurrentRow(self.lista_datos.count()-1)
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