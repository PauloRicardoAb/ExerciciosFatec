'''
Mostre todas as possibilidades de 2 dados de forma que a soma tenha como 
resultado 7.
'''

print("Possibilidades de 2 dados cuja soma é 7:")
print("Dado 1 | Dado 2 | Soma")
print("-" * 20)

contador = 0
for dado1 in range(1, 7):  # Dado 1: valores de 1 a 6
    for dado2 in range(1, 7):  # Dado 2: valores de 1 a 6
        if dado1 + dado2 == 7:
            print(f"  {dado1}    |   {dado2}    |  {dado1 + dado2}")
            contador += 1

print(f"\nTotal de possibilidades: {contador}")