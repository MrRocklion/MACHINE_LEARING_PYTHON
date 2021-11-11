import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk
plt.style.use("cyberpunk")
x = np.linspace(0,5,11)
y = x**2
print(x)
print(y)
#ejemplo 1
#imprimir datos de manera funciional
''' plt.plot(x,y,"r-") # el parametro r permite asignarle un color a la linea
plt.xlabel("X label") # permige agregar nombre a los ejes
plt.ylabel("Y label")
plt.title("Grafica Cuadratica") '''
#ejemplo 2
#imprimir varias graficas
'''

plt.subplot(1,2,1)
plt.plot(x,y,"r")
plt.subplot(1,2,2)
plt.plot(y,x,"b")   
'''
'''
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel("eje x")
axes.set_ylabel("eje y")
axes.set_title("Grafica orientada a objetos")

'''
'''
fig = plt.figure()
#paramteros figura 1
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y,'r')
axes1.set_title('Grafica grande')

#parametros figura 2
axes2 = fig.add_axes([0.6,0.6,0.4,0.3])
axes2.plot(y,x,'b')
axes2.set_title('Grafica pequeña')
'''
'''
fig, axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[0].set_title('grafica 1')
axes[1].plot(y,x)
axes[1].set_title('grafica 2')
plt.tight_layout()
'''
#uso de legenmda en matplotlib
'''
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.9,0.9])
ax.plot(x,y , label = 'funcion 1')
ax.plot(y,x,label = 'funcion 2')
ax.legend(loc=0)
'''
#personalizacion de las graficas

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.9,0.9])
ax.plot(x,y,label = 'cuadratic function', color= '#F1C40F',lw =2 , ls = '--')
ax.legend()
















plt.show()