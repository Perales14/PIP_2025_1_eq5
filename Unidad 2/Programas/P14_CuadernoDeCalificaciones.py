archivo = open("../../Archivos/Calificaciones_con_nombre.csv")
contenido = archivo.readlines()

print(contenido)

datos = [i.split(",") for i in contenido]

print(datos)

datos = [ [i[0], list(map(int,i[1:])) ] for i in datos]

print(datos)

datos = [[i[0],i[1],round(sum(i[1])/len(i[1]),2)] for i in datos]
print(datos)


for i in datos:
    print(f"El promedio de {i[0]} es {i[2]}")

promedios = [i[2] for i in datos]
nombres = [i[0] for i in datos]

promedioG = [sum(promedios)/len(promedios) for i in range(len(promedios))]

print(promedios)
promedios = sorted(promedios)
print(promedios)

# plt.plot(lis,lista, color = "black")
from matplotlib import pyplot as plt
plt.bar(nombres,promedios)
plt.plot(nombres,promedios,color = "red",marker = "x")
plt.plot(nombres,promedioG, color = "green")
plt.draw()
# print('12312sa')
plt.xlabel("Nombreaaa")
plt.ylabel("Calificaciones")
plt.show()
