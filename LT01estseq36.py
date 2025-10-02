'''
Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
'''

# Entrada de dados
n = int(input("Digite um número N: "))

# Função para calcular fatorial
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    fat = 1
    for i in range(2, num + 1):
        fat *= i
    return fat

# Cálculo da série
serie = 1  # Primeiro termo da série (1)
for i in range(1, n + 1):
    serie += 1 / fatorial(i)

print(f"A série 1 + 1/1! + 1/2! + ... + 1/{n}! = {serie:.6f}")