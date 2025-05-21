import sys
from PyQt5 import uic, QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

qtCreatorFile = "Vista_Grafica.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, tipo_sensor="distancia", datos=[]):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Graficar.clicked.connect(self.graficar_y_activar_auto)
        self.btn_Graficar_2.clicked.connect(self.limpiar_grafico)
        self.btn_Off.clicked.connect(self.cambiar_grilla)

        # Variables para la gráfica
        self.tipo_sensor = tipo_sensor
        self.datos = datos
        self.grilla_activada = False

        # Variable para controlar actualización automática
        self.auto_actualizacion = False

        # Timer para actualización automática
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_grafico)
        self.timer.setInterval(500)  # Actualizar cada 500 ms

        # Crear figura y lienzo
        self.figura = Figure(figsize=(8, 3), dpi=100)
        self.canvas = FigureCanvas(self.figura)
        self.verticalLayout.addWidget(self.canvas)

        # Actualizar título según el tipo de sensor
        self.actualizar_titulo()

        # No graficar automáticamente al inicio

    def actualizar_titulo(self):
        titulos = {
            "escaleras": "Gráfica de Escaleras",
            "foco_exterior": "Gráfica de Foco Exterior",
            "puerta_trasera": "Gráfica de Puerta Trasera",
            "temperatura": "Gráfica de Temperatura",
            "timbre": "Gráfica de Timbre",
            "distancia": "Gráfica de Distancia",
            "lluvia": "Gráfica de Lluvia"
        }

        if self.tipo_sensor in titulos:
            self.lbl_Home.setText(titulos[self.tipo_sensor])

    def graficar_y_activar_auto(self):
        # Graficar datos actuales
        self.graficar()

        # Activar actualización automática si no está activa
        if not self.auto_actualizacion:
            self.auto_actualizacion = True
            self.timer.start()

    def actualizar_grafico(self):
        if self.auto_actualizacion:
            self.graficar()

    def graficar(self):
        # Limpiar la figura
        self.figura.clear()

        # Agregar un subplot
        ax = self.figura.add_subplot(111)

        # Configurar la gráfica según el tipo de sensor
        if not self.datos:
            # Si no hay datos, mostrar mensaje
            ax.text(0.5, 0.5, "No hay datos disponibles",
                    horizontalalignment='center', verticalalignment='center',
                    transform=ax.transAxes, fontsize=14)
        else:
            # Crear x (índices)
            x = range(len(self.datos))

            # Graficar según el tipo de sensor
            if self.tipo_sensor in ["escaleras", "puerta_trasera", "timbre", "lluvia"]:
                # Sensores binarios (0/1)
                ax.step(x, self.datos, where='post', color='blue', marker='o')
                ax.set_yticks([0, 1])
                ax.set_yticklabels(['Apagado', 'Encendido'])
                ax.set_ylim(-0.1, 1.1)
            elif self.tipo_sensor == "foco_exterior":
                # LDR (0-4096)
                ax.plot(x, self.datos, color='orange', marker='o')
                ax.axhline(y=3000, color='r', linestyle='--', label='Umbral (3000)')
                ax.legend()
            elif self.tipo_sensor == "temperatura":
                # Temperatura
                ax.plot(x, self.datos, color='red', marker='o')
                ax.axhline(y=30, color='y', linestyle='--', label='Umbral (30°C)')
                ax.legend()
            elif self.tipo_sensor == "distancia":
                # Distancia
                ax.plot(x, self.datos, color='green', marker='o')

            # Configurar etiquetas
            ax.set_xlabel('Tiempo')
            ax.set_ylabel(self.obtener_etiqueta_y())

            # Configurar grilla
            ax.grid(self.grilla_activada)

        # Ajustar layout
        self.figura.tight_layout()

        # Actualizar el lienzo
        self.canvas.draw()

    def obtener_etiqueta_y(self):
        etiquetas = {
            "escaleras": "Estado",
            "foco_exterior": "Nivel de luz (0-4096)",
            "puerta_trasera": "Estado puerta",
            "temperatura": "Temperatura (°C)",
            "timbre": "Estado timbre",
            "distancia": "Distancia (cm)",
            "lluvia": "Estado lluvia"
        }

        return etiquetas.get(self.tipo_sensor, "Valor")

    def limpiar_grafico(self):
        # Detener actualización automática
        self.auto_actualizacion = False
        self.timer.stop()

        # Limpiar gráfico
        self.figura.clear()
        self.canvas.draw()

    def cambiar_grilla(self):
        self.grilla_activada = not self.grilla_activada
        self.btn_Off.setText("On" if self.grilla_activada else "Off")

        # Si la auto-actualización está activada, graficar inmediatamente para ver cambio
        if self.auto_actualizacion:
            self.graficar()

    def actualizar_datos(self, nuevos_datos):
        self.datos = nuevos_datos.copy()
        # Si auto-actualización está activada, graficar inmediatamente
        if self.auto_actualizacion:
            self.graficar()

    def closeEvent(self, event):
        # Detener el timer al cerrar la ventana para liberar recursos
        self.timer.stop()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())