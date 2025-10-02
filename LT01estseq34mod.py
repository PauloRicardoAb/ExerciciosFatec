'''
Receba um número. Calcule e mostre os resultados da tabuada desse número
'''

def tabuada(n):
    return [(n, i, n*i) for i in range(1, 11)]

def main():
    n = int(input("Digite um número: "))
    for _, i, r in tabuada(n):
        print(f"{n} x {i} = {r}")

if __name__ == "__main__":
    main()
