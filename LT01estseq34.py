'''
Receba um número. Calcule e mostre os resultados da tabuada desse número
'''

# Entrada de dados
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")