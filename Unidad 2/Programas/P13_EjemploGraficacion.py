
# y = mx + b
x = [i for i in range(-5,5+1,1)]
print(x)

m = 3
b = 2

y =[ v*m+b for v in x]

print(y)

from matplotlib import pyplot as plt
plt.plot(x,y,marker = "o")
plt.show()

#Practica 4 probar otras maneras de persoalizar el diseño de las graficas
# con matplotlib, osea cambiar cosas,