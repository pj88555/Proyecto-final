from scipy.misc import derivative
fx = lambda x: -x**2-x/2+4
h = [0.2,0.1]
xi = 0

# Derivación hacia adelante h^2
def derivada_adelante(fx,xi,h):
    fxim1 = fx(xi+h)
    fxim2 = fx(xi+2*h)
    return (-fxim2+4*fxim1-3*fx(xi))/(2*h)

# Derivación hacia atrás
def derivada_atras(fx,xi,h):
    fxim1 = fx(xi-h)
    fxim2 = fx(xi-2*h)
    return (3*fx(xi)-4*fxim1+fxim2)/(2*h)

# Derivación centrada
def derivada_centrada(fx,xi,h):
    fxip1 = fx(xi+h)
    fxip2 = fx(xi+2*h)
    fxim1 = fx(xi-h)
    fxim2 = fx(xi-2*h)
    return (-fxip2+8*fxip1-8*fxim1+fxim2)/(12*h)

print('*********** Valores reales o analíticos **************\n')
for h_i in h:
    print(f'La derivada analítica con h={h_i} es: {derivative(fx,xi,dx=h_i)}')

print('*********** Valores numéricos **************\n')
for h_i in h:
    print(f'La derivada hacia adelante con h={h_i} es: {derivada_adelante(fx,xi,h_i)}')
    print(f'La derivada hacia atrás con h={h_i} es: {derivada_atras(fx,xi,h_i)}')
    print(f'La derivada centrada con h={h_i} es: {derivada_centrada(fx,xi,h_i)}')
