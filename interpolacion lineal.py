def interpolacion_lineal(x0, y0, x1, y1, x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

x0, y0 = 3, 19
x1, y1 = 5, 99
x = 4

y = interpolacion_lineal(x0, y0, x1, y1, x)
print(f"Interpolación lineal entre f(3)={y0} y f(5)={y1}")
print(f"f({x}) ≈ {y}")
