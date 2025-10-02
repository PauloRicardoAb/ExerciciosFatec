'''
Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo 
do menor.
'''

def maior_multiplo_menor(a, b):
    maior = max(a, b)
    menor = min(a, b)
    return maior % menor == 0

def main():
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    if maior_multiplo_menor(x, y):
        print("O maior é múltiplo do menor.")
    else:
        print("O maior NÃO é múltiplo do menor.")

if __name__ == "__main__":
    main()
