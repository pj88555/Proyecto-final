import numpy as np 
from sympy import symbols, integrate, cos, exp

x = symbols('x')

f1_sym = 2 * cos(2 * x)
f2_sym = -x**2 - x/2 + 4
f3_sym = exp(-x**2)

f1 = lambda x: 2*np.cos(2*x)
f2 = lambda x: -x**2 - x/2 + 4
f3 = lambda x: np.exp(-x**2)

a = [0, 0.5, 0]
b = [np.pi/4, 1.5, 1]
funciones_sym = [f1_sym, f2_sym, f3_sym]
funciones_num = [f1, f2, f3]

def simpson_13(f, a, b):
    x1 = (a + b) / 2
    I = (b - a) * (f(a) + 4 * f(x1) + f(b)) / 6
    return round(I, 6)

def simpson_38(f, a, b):
    h = (b - a) / 3
    x1 = a + h
    x2 = a + 2*h
    I = 3*h * (f(a) + 3*f(x1) + 3*f(x2) + f(b)) / 8
    return round(I, 6)

print('----------Valores analíticos-------')
for i in range(len(funciones_sym)):
    integral = integrate(funciones_sym[i], (x, a[i], b[i]))
    print(f'Integral analítica de función {i}: {integral.evalf()}')

print('\n***Valores Simpson 1/3 *********')
for i in range(len(a)):
    print(f'Función {i} (1/3): {simpson_13(funciones_num[i], a[i], b[i])}')

print('\n***Valores Simpson 3/8 *********')
for i in range(len(a)):
    print(f'Función {i} (3/8): {simpson_38(funciones_num[i], a[i], b[i])}')
