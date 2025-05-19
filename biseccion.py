import numpy as np
import matplotlib.pyplot as plt

a = -3
b = -2
xr = -2.1913
num_interacciones = 5

xi = (a+b)/2
fx = lambda x: 2*x*np.cos(2*x)-(x+1)**2
er = lambda x1,xr: np.abs((xr-xi)/xr)*100

for i in range(1,num_interacciones+1):
    fa = fx(a)
    fb = fx(b)
    fxi = fx(xi)
    if fa * fxi < 0:
        b = xi
    else:
        a = xi
    xi = (a+b)/2
    error = er(xi, xr)
    print(f'i=f{i} / xi={xi} / fa={fa} / fb={fb} / er={error}\n')
    
x = np.linspace (-5,5,100)

plt.plot(x,fx(x))
plt.plot(xi,fx(xi),'ro')
plt.show()