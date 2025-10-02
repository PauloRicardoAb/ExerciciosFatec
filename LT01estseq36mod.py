'''
Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
'''

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

def serie_fatorial(n):
    return sum(1/fatorial(i) for i in range(0, n+1))

def main():
    n = int(input("Digite N: "))
    s = serie_fatorial(n)
    print(f"Série: {s:.6f}")

if __name__ == "__main__":
    main()
