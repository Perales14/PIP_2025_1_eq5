import serial as controlador

arduino = controlador.Serial("COM10",baudrate=9600,timeout=1)

datos = []
lectura = 0
tot_lecturas = 40

while lectura<tot_lecturas:
     cadena = arduino.readline().decode().strip()
     if cadena:
         # print(cadena)
         datos.append(cadena)
         lectura+=1


datos = [int(i) for i in datos]

print(datos)

from matplotlib import pyplot as plt
x = [i for i in range(len(datos))]
plt.plot(x,datos)
plt.show()
