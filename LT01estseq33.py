'''
Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N
'''

# Entrada de dados
n = int(input("Digite um número N: "))

# Cálculo da série
serie = 0
for i in range(1, n + 1):
    serie += 1 / i

print(f"A série 1 + 1/2 + 1/3 + ... + 1/{n} = {serie:.6f}")