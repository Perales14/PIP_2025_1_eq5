import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "../P07_PromedioNumeros-Load.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Agregar.clicked.connect(self.Agregar)
        self.btn_Guardar.clicked.connect(self.Guardar)
        self.btn_Cargar.clicked.connect(self.Cargar)
        self.txt_Calificacion.textChanged.connect(self.CheckLetterC)
        self.calificaciones = []

    def Cargar(self):
        #Comprobar si el archivo existe?
        #copiarlo, hacer el ejercicio 10, esto sera el ejercicio 10, lo de revisar que existe

        # archivo = open("../Archivos/calificaciones.csv")
        try:
           archivo = open("../../Archivos/calificaciones.csv")
        except Exception as error:
           print(error)
           self.msj("El archivo no existe")
           return

        contenido = archivo.readlines()
        print(contenido)
        datos = [float (x) for x in contenido]
        print(datos)
        #Ejercicio 11
        #En lugar de Sobreescribir, Concatenar
        self.calificaciones = datos
        self.promedio()
        #tarea 12
        #que solo se pueda cargar hasta antes de agregar la primera calificacion

    def promedio(self):
        prom = round(sum(self.calificaciones) / len(self.calificaciones),2)
        self.txt_Resultado.setText(str(prom))
    def Agregar(self):
        calificacion = float(self.txt_Calificacion.text())
        self.calificaciones.append(calificacion)
        prom = round(sum(self.calificaciones)/len(self.calificaciones),2)
        self.txt_Resultado.setText(str(prom))

    def Guardar(self):
        archivo = open ("../../Archivos/calificaciones.csv","w") #w = write, a = append
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
        
    def CheckLetterC(self):
        calificacion = self.txt_Calificacion.text()
        try:
            float(calificacion)
            calificacion = "".join(calificacion.split())
            self.txt_Calificacion.setText(calificacion)

        except:
            QtWidgets.QToolTip.showText(self.txt_Calificacion.mapToGlobal(self.txt_Calificacion.rect().bottomLeft()),
                                        "Solo se permiten números", None, QtCore.QRect(), 5000)
            self.txt_Calificacion.setFocus()
            calificacion = calificacion[:-1]
            self.txt_Calificacion.setText(calificacion)

    #Area de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())