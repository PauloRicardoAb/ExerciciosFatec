'''
Receba  um  número  in    print()  # Nova linha no finalo.  Calcule  e  mostre  a  série  de  Fibonacci  até  o  seu 
N'nésimo termo.
'''

# Entrada de dados
n = int(input("Digite o número de termos da série de Fibonacci: "))

if n <= 0:
    print("O número de termos deve ser positivo.")
elif n == 1:
    print("Série de Fibonacci:")
    print("0")
elif n == 2:
    print("Série de Fibonacci:")
    print("0, 1")
else:
    # Cálculo da série de Fibonacci
    print("Série de Fibonacci:")
    a, b = 0, 1
    print(f"{a}, {b}", end="")
    
    for i in range(2, n):
        proximo = a + b
        print(f", {proximo}", end="")
        a, b = b, proximo
    
    print()  # Nova linha no final