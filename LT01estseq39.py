'''
Calcule  a  quantidade  de  grãos  contidos  em  um  tabuleiro  de  xadrez  onde: 
Casa:  1 2 3 4 ...  64 
Qdte:  1 2 4 8 ...  N
'''

# O padrão é: casa 1 = 1 grão, casa 2 = 2 grãos, casa 3 = 4 grãos, etc.
# Ou seja, cada casa tem 2^(casa-1) grãos

total_graos = 0

print("Quantidade de grãos por casa:")
for casa in range(1, 65):  # 64 casas do tabuleiro
    graos_na_casa = 2 ** (casa - 1)
    total_graos += graos_na_casa
    print(f"Casa {casa}: {graos_na_casa} grãos")

print(f"\nTotal de grãos no tabuleiro: {total_graos}")

# Fórmula matemática: soma de progressão geométrica = 2^64 - 1
print(f"Verificação (2^64 - 1): {2**64 - 1}")