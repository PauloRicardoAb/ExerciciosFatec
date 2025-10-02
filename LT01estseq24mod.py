'''
Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
'''

def divisivel_por_2_e_3(n):
    return n % 2 == 0 and n % 3 == 0

def main():
    valor = int(input("Digite um valor inteiro: "))
    if divisivel_por_2_e_3(valor):
        print(f"{valor} é divisível por 2 e 3.")
    else:
        print(f"{valor} NÃO é divisível por 2 e 3.")

if __name__ == "__main__":
    main()
