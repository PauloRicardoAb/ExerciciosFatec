'''
Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99 
'''

# Padrão da série: numerador de 1 a 50, denominador de 1 a 99 (ímpares: 1, 3, 5, 7, ..., 99)
soma_serie = 0

print("Série: 1 + 2/3 + 3/5 + ... + 50/99")
print("\nTermos da série:")

for i in range(1, 51):  # numerador de 1 a 50
    numerador = i
    denominador = 2 * i - 1  # denominadores ímpares: 1, 3, 5, 7, ..., 99
    termo = numerador / denominador
    soma_serie += termo
    
    if i <= 10:  # Mostra os primeiros 10 termos
        print(f"{numerador}/{denominador} = {termo:.6f}")
    elif i == 11:
        print("...")

print(f"\nSoma da série: {soma_serie:.6f}")