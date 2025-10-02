'''
Receba  2  números  inteiros,  verifique  qual  o  maior  entre  eles.  Calcule  e 
mostre o resultado da somatória dos números ímpares entre esses valores. 
'''

# Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Determina o menor e maior número
menor = min(num1, num2)
maior = max(num1, num2)

# Cálculo da somatória dos números ímpares
soma_impares = 0
for numero in range(menor, maior + 1):
    if numero % 2 != 0:  # Verifica se é ímpar
        soma_impares += numero

print(f"A somatória dos números ímpares entre {menor} e {maior} é: {soma_impares}")