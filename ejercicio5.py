import random

N = 5

def multiplos_fila(N):
    v = [random.randint(1, 10) for _ in range(N)]
    print('vector aleatorio:', v)
    
    matriz = []
    for i in range(N):
        fila = [v[i] * (j + 1) for j in range(N)] 
        matriz.append(fila)
    
    print('matriz de múltiplos en filas:')
    for fila in matriz:
        print(fila)

def multiplos_columna(N):
    v = [random.randint(1, 10) for _ in range(N)]
    print('\nvector aleatorio:', v)
    
    matriz = []
    for i in range(N):
        fila = [v[j] * (i + 1) for j in range(N)] 
        matriz.append(fila)
    
    print('matriz de múltiplos en columnas:')
    for fila in matriz:
        print(fila)

multiplos_fila(N)
multiplos_columna(N)
