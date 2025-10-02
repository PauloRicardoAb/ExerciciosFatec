# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre
# a hipotenusa

import math

cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print(f"A hipotenusa é: {hipotenusa}")