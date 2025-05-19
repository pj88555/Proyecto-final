import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 3, 5])
y = np.array([6, 19, 99])

coef = np.polyfit(x, y, 2)
polinomio = np.poly1d(coef)

f_4 = polinomio(4)
print(f"Estimación cuadrática: f(4) ≈ {f_4}")

x_vals = np.linspace(min(x), max(x), 200)
y_vals = polinomio(x_vals)

plt.plot(x, y, 'ro', label='Puntos dados')
plt.plot(x_vals, y_vals, 'b-', label='Interpolación cuadrática')
plt.scatter(4, f_4, color='black', zorder=5)
plt.title("Interpolación Cuadrática ")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
