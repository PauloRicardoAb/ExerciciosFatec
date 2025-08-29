"""Receba  3  coeficientes  A,  B  e  C  de  uma  equação  do  2º  grau  da  fórmula 
AX²+BX+C=0.  Verifique  e  mostre  a  existência  de  raízes  reais  e  se  caso 
exista, calcule e mostre.
"""

A = int(input('Valor de A: '))
B = int(input('Valor de B: '))
C = int(input('Valor de C: '))

if A == 0:
    print("Não é uma equação do 2º grau.")
else:
    delta = B**2 - 4*A*C
    print(f"Delta: {delta}")
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -B / (2*A)
        print(f"Existe uma raiz real: x = {x}")
    else:
        x1 = (-B + delta**0.5) / (2*A)
        x2 = (-B - delta**0.5) / (2*A)
        print(f"Existem duas raízes reais: x1 = {x1}, x2 = {x2}")