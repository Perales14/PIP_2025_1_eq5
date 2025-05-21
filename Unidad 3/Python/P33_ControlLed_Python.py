import serial as controlador

arduino = controlador.Serial("COM10",baudrate=9600,timeout=1)

lectura = 0
tot_lecturas = 25

while lectura<tot_lecturas:
     accion = input("ingresa el valor: ")
     arduino.write(accion.encode())
