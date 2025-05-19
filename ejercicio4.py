import random

N = 3

def Matriz(N):
    v = [random.randint(1, 10) for _ in range(N)]
    print("vector aleatorio:", v)
    
    matriz = []
    for j in range(N):
        columna = [v[i] * (j + 1) for i in range(N)]  
        matriz.append(columna)
    
    return matriz

for fila in Matriz(N):
    print(fila)
