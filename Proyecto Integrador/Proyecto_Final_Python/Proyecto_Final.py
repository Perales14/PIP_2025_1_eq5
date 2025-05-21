import sys
import random
import time
from PyQt5 import uic, QtWidgets, QtCore
import Dialogo_ConexionArduino
import Vista_Distancia
import Vista_Escaleras
import Vista_FocoExterior
import Vista_Lluvia
import Vista_PuertaTrasera
import Vista_Temperatura
import Vista_Timbre

qtCreatorFile = "Proyecto_Final.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.arduino = None

        # Botón de conexión
        self.btn_Conectar.clicked.connect(self.iniciar)

        # Botones de servicios
        self.btn_Escaleras.clicked.connect(self.mostrar_escaleras)
        self.btn_Timbre.clicked.connect(self.mostrar_timbre)
        self.btn_FocoExterior.clicked.connect(self.mostrar_foco_exterior)
        self.btn_Distancia.clicked.connect(self.mostrar_distancia)
        self.btn_Lluvia.clicked.connect(self.mostrar_lluvia)
        self.btn_PuertaTrasera.clicked.connect(self.mostrar_puerta_trasera)
        self.btn_7.clicked.connect(self.mostrar_temperatura)  # Temperatura

        # Configuración para simulación
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.simulacion_y_lecturas)

        self.bandera = 0
        self.datos = []
        self.envio = 0

        self.escaleras = True
        self.focoxt = True
        self.lluvia = True
        self.puerta = True
        self.abanico = True #temperatura


        # Variables para simular los sensores
        self.pir_datos = [0, 0]  # Escaleras: dos sensores PIR
        self.ldr_dato = 0  # Foco exterior: valores entre 0-4096
        self.boton_matriz_input = "N"  # Puerta trasera: entrada del botón matriz
        self.boton_matriz_password = ""  # Contraseña ingresada
        self.contrasena_correcta = "1234"  # Contraseña por defecto
        self.temperatura_dato = 25  # Temperatura en grados
        self.timbre_dato = 0  # Timbre: 0/1
        self.distancia_dato = 50  # Distancia en cm (10-100)
        self.lluvia_dato = 0  # Lluvia: 0/1
        self.nivel_porcentaje = 0  # Porcentaje de llenado del tinaco

        # Constantes para distancia
        self.VACIO = 100  # cm
        self.LLENO = 10  # cm

        # Estados de los servicios
        self.escaleras_estado = 0  # 0: apagado, 1: encendido
        self.foco_exterior_estado = 0
        self.puerta_trasera_estado = 0
        self.abanico_estado = 0
        self.buzzer_estado = 0
        self.tendedero_estado = 0

        # Historial de datos para gráficas
        self.historial_escaleras = []
        self.historial_foco_exterior = []
        self.historial_puerta_trasera = []
        self.historial_temperatura = []
        self.historial_timbre = []
        self.historial_distancia = []
        self.historial_lluvia = []

        # Instancias de las ventanas
        self.ventana_escaleras = None
        self.ventana_foco_exterior = None
        self.ventana_puerta_trasera = None
        self.ventana_temperatura = None
        self.ventana_timbre = None
        self.ventana_distancia = None
        self.ventana_lluvia = None
        self.ventana_grafica = None

    # Área de los Slots
    def iniciar(self):
        self.dialogo = Dialogo_ConexionArduino.MyApp(self)
        self.dialogo.show()

    def leer_datos(self):
        try:
            linea = self.arduino.readline()
            if not linea:
                return  # No se recibió nada

            cadena = linea.decode('utf-8', errors='ignore').strip()
            datos = cadena.split("-")


            if len(datos) != 8:
                print(f"Formato incorrecto, se esperaban 8 datos, se recibieron {len(datos)}: {cadena}")
                return

            # Depuración opcional
            print("Cadena recibida:", cadena)

            # Asignar valores
            self.pir_datos[0] = int(datos[0])  # PIR1
            self.pir_datos[1] = int(datos[1])  # PIR2
            self.ldr_dato = int(datos[2])  # LDR
            self.boton_matriz_input = datos[3]  # Botón matriz (letra, número, #, * o "N")
            self.temperatura_dato = float(datos[4])  # Temperatura
            self.timbre_dato = int(datos[5])  # Timbre
            self.distancia_dato = float(datos[6])  # Distancia
            self.lluvia_dato = int(datos[7])  # Lluvia



        except (ValueError, IndexError) as e:
            print(f"Error de conversión o índice en datos recibidos: {cadena} -> {e}")
        except Exception as e:
            print(f"Error al leer o procesar datos del Arduino: {e}")

    def enviar_datos(self):
        # Construir la cadena de datos a enviar
        datos = [
            self.escaleras_estado,
            self.foco_exterior_estado,
            self.puerta_trasera_estado,
            self.abanico_estado,
            self.buzzer_estado,
            self.nivel_porcentaje,
            self.tendedero_estado
        ]
        # cadena
        # cadena = "-".join(map(str, datos)) + "\n"  # Añade salto de línea al final
        cadena = str(self.escaleras_estado ) + "-"
        cadena += str(self.foco_exterior_estado) + "-"
        cadena += str(self.puerta_trasera_estado) + "-"
        cadena += str(self.abanico_estado) + "-"
        cadena += str(self.buzzer_estado) + "-"
        cadena += str(self.nivel_porcentaje) + "-"
        cadena += str(self.tendedero_estado)


        # Enviar la cadena al Arduino si el puerto está disponible
        if self.arduino and self.arduino.isOpen():
            try:
                self.arduino.write(cadena.encode('utf-8'))
                print("Datos enviados al Arduino:", cadena.strip())
            except Exception as e:
                print("Error al enviar datos al Arduino:", e)
        else:
            print("Puerto no disponible para enviar datos al Arduino.")

    def simulacion_y_lecturas(self):
        if self.arduino and self.arduino.isOpen():
            # En un caso real, aquí se leerían los datos del Arduino
            # Como no tenemos Arduino físico, simulamos los datos
            # self.simular_datos_sensores()
            self.envio += 1
            if self.envio == 5:  # Enviar cada 10 ciclos
                self.enviar_datos()
                self.envio = 0
            self.leer_datos()

            self.procesar_datos()
            self.actualizar_historial()

            # Crear cadena simulada como si viniera del Arduino
            cadena = f"{self.pir_datos[0]}-{self.pir_datos[1]}-{self.ldr_dato}-{self.boton_matriz_input}-{self.temperatura_dato}-{self.timbre_dato}-{self.distancia_dato}-{self.lluvia_dato}"

            # Guardar en la lista de datos
            self.datos.append(cadena)

            if self.bandera == 0:
                print(cadena)

                # Actualizar las vistas si están abiertas
                self.actualizar_vistas()

    def procesar_datos(self):
        #Escaleras: Si cualquiera de los dos sensores PIR detecta movimiento, se encienden
        if self.escaleras:
            if self.pir_datos[0] == 1 or self.pir_datos[1] == 1:
                self.escaleras_estado = 1
            else:
                self.escaleras_estado = 0

        # 2. Foco exterior: Si el valor LDR supera 3000, se enciende
        if self.focoxt:
            if self.ldr_dato >= 3000:
                self.foco_exterior_estado = 1
            else:
                self.foco_exterior_estado = 0

        #Puerta trasera: Procesar entrada del botón matriz
        if self.puerta:
            if self.boton_matriz_input == "#":
                # Inicio de ingreso de contraseña
                self.boton_matriz_password = ""
            elif self.boton_matriz_input == "*":
                # Fin de ingreso de contraseña, verificar
                if self.boton_matriz_password == self.contrasena_correcta:
                    self.puerta_trasera_estado = 1  # Abrir puerta
                else:
                    self.puerta_trasera_estado = 0  # Mantener cerrada
            elif self.boton_matriz_input != "N":
                # Agregar dígito a la contraseña
                self.boton_matriz_password += self.boton_matriz_input

        #Timbre: Pasar directamente el estado
        self.buzzer_estado = self.timbre_dato

        #Distancia (Tinaco): Calcular porcentaje de llenado
        #Fórmula: % = 100 * (VACIO - medición) / (VACIO - LLENO)
        self.nivel_porcentaje = 100 * (self.VACIO - self.distancia_dato) / (self.VACIO - self.LLENO)
        self.nivel_porcentaje = max(0, min(100, int(self.nivel_porcentaje)))  # Limitar entre 0% y 100%

        # 6. Abanico: Se enciende si la temperatura es mayor a 30 grados
        if self.abanico:
            if self.temperatura_dato > 45:
                self.abanico_estado = 1
            else:
                self.abanico_estado = 0

        # 7. Lluvia: Controla el tendedero
        if self.lluvia:
            self.tendedero_estado = self.lluvia_dato

    def actualizar_historial(self):
        # Mantener solo las últimas 20 lecturas para cada sensor
        max_historial = 20

        # Historial de escaleras
        self.historial_escaleras.append(self.escaleras_estado)
        if len(self.historial_escaleras) > max_historial:
            self.historial_escaleras.pop(0)

        # Historial de foco exterior
        self.historial_foco_exterior.append(self.ldr_dato)
        if len(self.historial_foco_exterior) > max_historial:
            self.historial_foco_exterior.pop(0)

        # Historial de puerta trasera
        self.historial_puerta_trasera.append(self.puerta_trasera_estado)
        if len(self.historial_puerta_trasera) > max_historial:
            self.historial_puerta_trasera.pop(0)

        # Historial de temperatura
        self.historial_temperatura.append(self.temperatura_dato)
        if len(self.historial_temperatura) > max_historial:
            self.historial_temperatura.pop(0)

        # Historial de timbre
        self.historial_timbre.append(self.timbre_dato)
        if len(self.historial_timbre) > max_historial:
            self.historial_timbre.pop(0)

        # Historial de distancia
        self.historial_distancia.append(self.distancia_dato)
        if len(self.historial_distancia) > max_historial:
            self.historial_distancia.pop(0)

        # Historial de lluvia
        self.historial_lluvia.append(self.lluvia_dato)
        if len(self.historial_lluvia) > max_historial:
            self.historial_lluvia.pop(0)

    def mostrar_escaleras(self):
        self.ventana_escaleras = Vista_Escaleras.MyApp(parent=self)
        self.ventana_escaleras.show()

    def mostrar_foco_exterior(self):
        self.ventana_foco_exterior = Vista_FocoExterior.MyApp(parent=self)
        self.ventana_foco_exterior.show()

    def mostrar_puerta_trasera(self):
        self.ventana_puerta_trasera = Vista_PuertaTrasera.MyApp(parent=self)
        self.ventana_puerta_trasera.show()
        pass

    def mostrar_temperatura(self):
        self.ventana_temperatura = Vista_Temperatura.MyApp(parent=self)
        self.ventana_temperatura.show()
        pass

    def mostrar_timbre(self):
        self.ventana_timbre = Vista_Timbre.MyApp(parent=self)
        self.ventana_timbre.show()
        pass

    def mostrar_distancia(self):
        self.ventana_distancia = Vista_Distancia.MyApp(parent=self)
        self.ventana_distancia.show()

    def mostrar_lluvia(self):
        self.ventana_lluvia = Vista_Lluvia.MyApp(parent=self)
        self.ventana_lluvia.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())