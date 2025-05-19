import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv')

X = df ['Experience Years']
Y = df ['Salary']
sum_xiyi = sum(X*Y)
sum_xi2 = sum(X**2)
n = len(X)

a1 = (n*sum_xiyi-sum(X)*sum(Y))/(n*sum_xi2-sum(X)**2)
a0 = (sum(Y)/n)-a1*(sum(X)/n)

x_grafica = np.linspace(min(X),max(X),100)
y_grafica = a0+a1*x_grafica
y_regresion = lambda x : a0+a1*x
datos_estimar = [15,30,50]
for dato in datos_estimar:
    print(f'Años {dato}: salario {y_regresion(dato)}')

plt.xlabel('Experiencia en años')
plt.ylabel('Salario')
plt.plot(x_grafica,y_grafica)
plt.plot(X,Y,'o')
plt.grid()
plt.show()