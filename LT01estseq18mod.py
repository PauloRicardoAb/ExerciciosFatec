'''
Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
'''

def diferenca_maior_menor(a, b):
    return abs(a - b)

def main():
    x = int(input("Primeiro valor inteiro: "))
    y = int(input("Segundo valor inteiro: "))
    print(f"Diferença do maior pelo menor: {diferenca_maior_menor(x, y)}")

if __name__ == "__main__":
    main()
