import numpy as np
import matplotlib.pyplot as plt

x0 = 0.3
num_interacciones = 5

fx = lambda x: 8*x*np.sin(x)*np.exp(-x)-1
dfx = lambda x: 8*np.exp(-x)*(np.sin(x)+x*np.cos(x)-x*np.sin(x))
er = lambda xi,x0: np.abs((xi-x0)/xi)*100

for i in range(1,num_interacciones+1):
    fx0 = fx(x0)  
    dfx0 = dfx(x0)
    xi = x0 - fx0 / dfx0
    error = er(xi, x0)
    print(f'i=f{i} / xi={xi} / er={error}\n')
    x0 = xi
    
x = np.linspace (-5,5,100)

plt.plot(x,fx(x))
plt.plot(xi,fx(xi),'ro')
plt.show()