# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.


angulo1 = float(input("Digite o valor do primeiro ângulo (em graus): "))
angulo2 = float(input("Digite o valor do segundo ângulo (em graus): "))

angulo3 = 180 - (angulo1 + angulo2)

print(f"O valor do terceiro ângulo é: {angulo3} graus")