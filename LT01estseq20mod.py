'''
Receba  3  coeficientes  A,  B  e  C  de  uma  equação  do  2º  grau  da  fórmula 
AX²+BX+C=0.  Verifique  e  mostre  a  existência  de  raízes  reais  e  se  caso 
exista, calcule e mostre. 
'''
import math

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)

def main():
    a = float(input("Coeficiente A: "))
    b = float(input("Coeficiente B: "))
    c = float(input("Coeficiente C: "))
    raizes = calcular_raizes(a, b, c)
    if raizes is None:
        print("Não existem raízes reais.")
    elif len(raizes) == 1:
        print(f"Raiz única: {raizes[0]:.2f}")
    else:
        print(f"Raízes: {raizes[0]:.2f} e {raizes[1]:.2f}")

if __name__ == "__main__":
    main()
