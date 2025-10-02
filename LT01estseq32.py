'''
Receba um número inteiro. Calcule e mostre o seu fatorial.
'''

# Entrada de dados
numero = int(input("Digite um número inteiro: "))

# Verificação se o número é não-negativo
if numero < 0:
    print("Fatorial não está definido para números negativos.")
else:
    # Cálculo do fatorial
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"O fatorial de {numero} é: {fatorial}")