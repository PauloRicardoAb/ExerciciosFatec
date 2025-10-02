'''
Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
'''

def ordem_crescente(a, b):
    return tuple(sorted([a, b]))

def main():
    x = int(input("Primeiro valor inteiro: "))
    y = int(input("Segundo valor inteiro: "))
    if x == y:
        print("Os valores devem ser diferentes!")
    else:
        menor, maior = ordem_crescente(x, y)
        print(f"Ordem crescente: {menor}, {maior}")

if __name__ == "__main__":
    main()
