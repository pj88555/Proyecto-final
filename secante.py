import numpy as np
import matplotlib.pyplot as plt

x0 = 0.3
x1 = 0.5
num_interacciones = 5

fx = lambda x: 8*x*np.sin(x)*np.exp(-x)-1
er = lambda x2,x1: np.abs((x2-x1)/x2)*100

for i in range(1,num_interacciones+1):
    fx0 = fx(x0)
    fx1 = fx(x1)
    x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
    error = er(x2, x1)
    x0 = x1
    x1 = x2
    print(f'i=f{i} / x1={x1} / x2={x2} / er={error}\n')
    
x = np.linspace (-5,5,100)

plt.plot(x,fx(x))
plt.plot(x2,fx(x2),'ro')
plt.show()
