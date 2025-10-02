'''
Receba  o  número  da  base  e  do  expoente.  Calcule  e  mostre  o  valor  da 
potência.
'''

# Entrada de dados
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Cálculo da potência
if expoente == 0:
    resultado = 1
elif expoente > 0:
    resultado = 1
    for i in range(expoente):
        resultado *= base
else:  # expoente negativo
    resultado = 1
    for i in range(abs(expoente)):
        resultado *= base
    resultado = 1 / resultado

print(f"{base}^{expoente} = {resultado}")