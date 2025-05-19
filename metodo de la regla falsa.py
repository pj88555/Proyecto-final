import numpy as np
import matplotlib.pyplot as plt

a = -3
b = -2
xr = -2.1913
num_interacciones = 5

fx = lambda x: 2*x*np.cos(2*x)-(x+1)**2
er = lambda xi,xr: np.abs((xr-xi)/xr)*100

for i in range(1,num_interacciones+1):
    fa = fx(a)
    fb = fx(b)
    xi = b - (fb * (a - b)) / (fa - fb)    
    fxi = fx(xi)
    error = er(xi, xr)
    print(f'i=f{i} / a{a} / b{b} / fa={fa} / fb={fb} / xi{xi} / er={error}\n')
    if fa * fxi < 0:
        b = xi
    else:
        a = xi
    
x = np.linspace (-5,5,100)

plt.plot(x,fx(x))
plt.plot(xi,fx(xi),'ro')
plt.show()
