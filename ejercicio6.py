import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20,20,100)

y1 = np.sin(x)
y2 = np.tan(x) 
y3 = np.cos(x)

plt.title('Funciones trigonometricas')
plt.plot(x,y1,'ro-',label='sin(x)')
plt.plot(x,y2,'b*-',label='tan(x)')
plt.plot(x,y3,'g^:',label='cos(x)')
plt.legend(loc = 'best')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid()
plt.show()