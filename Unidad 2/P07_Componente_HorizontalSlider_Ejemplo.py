import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_Componente_HorizontalSlider_Ejemplo.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#Comando para crear el Recursos_rc.py, desde "archivos" y lo cree en esta carpeta, no alla
# pyrcc5 .\Recursos.qrc -o '..\Unidad 2\Recursos_rc.py'
# como tal el codigo es
#asi lo creara en la carpeta en la que se encuentre
# pyrcc5 .\Recursos.qrc -o Recursos_rc.py
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dial.setMinimum(-50)
        self.dial.setMaximum(+50)
        self.dial.setSingleStep(5)
        self.dial.setValue(50)
        self.dial.valueChanged.connect(self.cambiarValor)
        self.txt_valor.setText("-50")
# Area de los Signals

    def cambiarValor(self):
        value = self.dial.value()
        self.txt_valor.setText(str(value))


#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())