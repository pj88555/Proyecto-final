import numpy as np 

A = np.array([[1, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, -10]], dtype=float)
b = np.array([7.85, 19.3, 71.4], dtype=float)

n = len(b)

def error_relativo(xi, xr):
    return np.max(np.abs((xi - xr) / xi))

def jacobi(A, b, num_iteraciones=3):
    x = np.zeros_like(b) 
    x_old = np.copy(x)  
    for i in range(1, num_iteraciones + 1):
        for j in range(n):
            sum_ = b[j]
            for k in range(n):
                if k != j:
                    sum_ -= A[j, k] * x_old[k]
            x[j] = sum_ / A[j, j]

        error = error_relativo(x, x_old)
        print(f"Iteración {i} / x={x} / Error Relativo={error}")
        x_old = np.copy(x)
    return x

def gauss_seidel(A, b, num_iteraciones=3):
    x = np.zeros_like(b)  
    x_old = np.copy(x)  

    for i in range(1, num_iteraciones + 1):
        for j in range(n):
            sum_ = b[j]
            for k in range(n):
                if k != j:
                    sum_ -= A[j, k] * x[k]
            x[j] = sum_ / A[j, j]

        error = error_relativo(x, x_old)
        print(f"Iteración {i} / x={x} / Error Relativo={error}")

        x_old = np.copy(x)

    return x

num_iteraciones = 3

print("\nMétodo de Jacobi:")
jacobi(A, b, num_iteraciones)

print("\nMétodo de Gauss-Seidel:")
gauss_seidel(A, b, num_iteraciones)
