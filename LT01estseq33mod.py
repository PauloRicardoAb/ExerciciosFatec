'''
Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
'''

def serie_harmonica(n):
    return sum(1/i for i in range(1, n+1))

def main():
    n = int(input("Digite N: "))
    s = serie_harmonica(n)
    print(f"Série: {s:.6f}")

if __name__ == "__main__":
    main()
