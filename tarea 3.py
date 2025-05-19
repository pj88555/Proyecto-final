import numpy as np

A = np.array([[1, 1, 1], [1, 2, 5], [1, 4, 25]])
b = np.array([6, 12, 36])

det_A = np.linalg.det(A)

if det_A != 0:
    x_solve = np.linalg.solve(A, b)
    print("\nSolución usando np.linalg.solve:", x_solve)

    A_inv = np.linalg.inv(A)
    x_inv = np.matmul(A_inv, b) 
    print("\nSolución usando np.linalg.inv y np.matmul:", x_inv)

    x_det_method = np.matmul(np.linalg.inv(A), b)
    print("\nSolución usando el determinante (A^(-1) * b):", x_det_method)

def lu_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)  
    U = np.zeros_like(A)  

    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

        L[i, i] = 1

    return L, U

L, U = lu_decomposition(A)
print("\nDescomposición LU usando Doolittle:")
print("Matriz L:")
print(L)
print("Matriz U:")
print(U)

def cholesky_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)  

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i, i] = np.sqrt(A[i, i] - np.dot(L[i, :i], L[i, :i]))
            else:
                L[i, j] = (A[i, j] - np.dot(L[i, :j], L[j, :j])) / L[j, j]
    return L

if np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0):
    L_chol = cholesky_decomposition(A)
    print("\nDescomposición de Cholesky:")
    print("Matriz L (de Cholesky):")
    print(L_chol)
else:
    print("\nLa matriz A no es simétrica o no es positiva definida para Cholesky.")
