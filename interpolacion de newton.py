import numpy as np
import matplotlib.pyplot as plt

def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1]) / (x[j:n] - x[j - 1])
    return coef

def polinomio_newton(coef, x_data, x):
    n = len(coef)
    p = coef[0]
    for k in range(1, n):
        p *= 1  
        p += coef[k] * np.prod(x - x_data[:k])
    return p

x = np.array([1, 2, 3, 5, 7])
y = np.array([3, 6, 19, 99, 291])

coef = diferencias_divididas(x, y)
x_vals = np.linspace(min(x), max(x), 300)
y_vals = [polinomio_newton(coef, x, xi) for xi in x_vals]

f_4 = polinomio_newton(coef, x, 4)
print(f"Estimación de Newton (orden 4): f(4) ≈ {f_4}")

plt.plot(x, y, 'ro', label='Puntos dados')
plt.plot(x_vals, y_vals, 'g-', label='Interpolación de Newton')
plt.scatter(4, f_4, color='black', zorder=5)
plt.title("Interpolación de Newton ")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

