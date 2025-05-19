import numpy as np
import matplotlib.pyplot as plt

x0 = 0.8
num_interacciones = 10
coef = [1, -5, 5, -1] 

fx = lambda x: x**3 - 5*x**2 + 5*x-1
dfx = lambda x: 3*x**2 - 10*x + 5
def division_sintetica(coef, x0):
    n = len(coef)
    nuevo_coef = [coef[0]]  
    for i in range(1, n):
        nuevo_coef.append(coef[i] + nuevo_coef[i - 1] * x0)
    return nuevo_coef

for i in range(1,num_interacciones+1):
    fx0 = fx(x0)  
    dfx0 = dfx(x0)
    xi = x0 - fx0 / dfx0
    print(f'i=f{i} / xi={xi}')
    nuevo_coef = division_sintetica(coef, x0 if i == 1 else xi)
    print(f"División sintética {nuevo_coef}")
    x0 = xi
    
a, b, c = nuevo_coef[0], nuevo_coef[1], nuevo_coef[2]

discriminante = b**2 - 4*a*c
if discriminante >= 0:
    x1 = (-b + np.sqrt(discriminante)) / (2*a)
    x2 = (-b - np.sqrt(discriminante)) / (2*a)
    print(f"Raíces : x1 = {x1}, x2 = {x2}")
else:
    print("Las raíces restantes no son reales.")
    
    
x = np.linspace (-5,5,100)

plt.plot(x,fx(x))
plt.plot(xi,fx(xi),'ro')
plt.show()