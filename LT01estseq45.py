'''
Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
'''
soma_serie = 0

print("Série: 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225")
print("\nTermos da série:")

for i in range(1, 16):  # de 1 a 15
    numerador = i
    denominador = i ** 2
    termo = numerador / denominador
    
    # Determina o sinal (alternado começando com +)
    if i % 2 == 1:  # ímpar: sinal positivo
        soma_serie += termo
        sinal = "+"
    else:  # par: sinal negativo
        soma_serie -= termo
        sinal = "-"
    
    if i == 1:
        print(f"{numerador}/{denominador} = {termo:.6f}")
    else:
        print(f"{sinal} {numerador}/{denominador} = {sinal}{termo:.6f}")

print(f"\nSoma da série: {soma_serie:.6f}")