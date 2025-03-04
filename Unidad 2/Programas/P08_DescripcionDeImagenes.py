import sys
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "P08_DescripcionDeImagenes.ui" # Nombre del archivo aqui
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
        self.selector_Imagen.setMinimum(1)
        self.selector_Imagen.setMaximum(1)
        self.selector_Imagen.setSingleStep(1)
        self.selector_Imagen.setValue(1)
        self.selector_Imagen.valueChanged.connect(self.cambiarValor)
        # self.diccionarioDatos ={
        #     0: (":/Images/Gatos.png",["Gato", "4 meses", "Raton"]),
        #     0: (":/Logos/FIT_logo_vertical.png", ["Castor","65 años", "e"]),
        #     0: (":/Logos/log_uat_nuevo.png", []),
        # }

        # self.txt_Nombre.setText("1")
# Area de los Signals

    def cambiarValor(self):
        value = self.dial.value()
        # self.txt_valor.setText(str(value))


#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())