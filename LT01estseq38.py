'''
Receba  100  números  inteiros  reais.  Verifique  e  mostre  o  maior  e  o  menor 
valor. Obs.: somente valores positivos.
'''

# Inicialização das variáveis
maior = 0
menor = float('inf')  # Inicializa com infinito

print("Digite 100 números positivos:")

# Loop para receber 100 números
for i in range(1, 101):
    while True:
        numero = float(input(f"Digite o {i}º número: "))
        if numero > 0:
            break
        else:
            print("Apenas valores positivos são aceitos. Digite novamente.")
    
    # Verifica se é o primeiro número ou atualiza maior/menor
    if i == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"\nMaior valor: {maior}")
print(f"Menor valor: {menor}")