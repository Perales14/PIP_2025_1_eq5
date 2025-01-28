import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P06_PromedioNumeros-Save.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Agregar.clicked.connect(self.Agregar)
        self.btn_Guardar.clicked.connect(self.Guardar)
        self.calificaciones = []

    def Agregar(self):
        calificacion = int(self.txt_Calificacion.text())
        self.calificaciones.append(calificacion)
        prom = sum(self.calificaciones)/len(self.calificaciones)
        self.txt_Resultado.setText(str(prom))

    def Guardar(self):
        archivo = open ("../Archivos/calificaciones.csv","w") #w = write, a = append
        for c in self.calificaciones:
            archivo.write(str(c))
            archivo.write("\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo guardado bien")
    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)

        m.exec_()

    #Area de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())