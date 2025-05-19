import random

N = 5

def Matriz(N):
    v = [random.randint(1, 10) for _ in range(N)]
    print("vector aleatorio:", v)
    
    matriz = []
    for i in range(N):
        fila = [v[i] * (j + 1) for j in range(N)]  
        matriz.append(fila)
    
    return matriz

for fila in Matriz(N):
    print(fila)
