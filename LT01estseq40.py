'''
Receba  2  números  inteiros.  Verifique  e  mostre  todos  os  números  primos 
existentes entre eles
'''

def eh_primo(num):
    """Função para verificar se um número é primo"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Determina o menor e maior número
menor = min(num1, num2)
maior = max(num1, num2)

print(f"\nNúmeros primos entre {menor} e {maior}:")
primos_encontrados = []

for numero in range(menor, maior + 1):
    if eh_primo(numero):
        primos_encontrados.append(numero)

if primos_encontrados:
    for primo in primos_encontrados:
        print(primo, end=" ")
    print(f"\n\nTotal de números primos encontrados: {len(primos_encontrados)}")
else:
    print("Não há números primos neste intervalo.")