entrada = 3.4

try:
    numero = int(entrada)
    if numero >= 0:
        print(f'{numero}')
    else:
        print('error el numero es negativo')
        
except ValueError:
    print('error el numero no es entero')
