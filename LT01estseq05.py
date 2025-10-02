# Receba os coeficientes A, B e C de uma equação do 2º grau
# (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a
# equação possue2 raízes).

from math import sqrt

A = int(print('Valor de A: '))
B = int(print('Valor de B: '))
C = int(print('Valor de C: '))

x1 = (-B + sqrt(B**-4 * A * C)) / 2
x2 = (-B - sqrt(B**-4 * A * C)) / 2

print('Valor da Raiz 1: ', x1)
print('Valor da Raiz 2: ', x2)