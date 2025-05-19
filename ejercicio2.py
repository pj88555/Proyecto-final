import random

entrada = 2.3

try:
    numero = int(entrada)
    if numero >= 0:
        vector = [random.randint(1, 9) for _ in range(numero)]
        print(f'Vector de {numero} elementos aleatorios entre 1 y 9:')
        print(vector)
    else:
        print('Error: el numero debe ser positivo')
except ValueError:
    print('error el numero no es entero')
