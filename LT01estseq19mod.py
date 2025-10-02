'''
Receba 2 valores reais. Calcule e mostre o maior deles.
'''

def maior_valor(a, b):
    return max(a, b)

def main():
    x = float(input("Primeiro valor real: "))
    y = float(input("Segundo valor real: "))
    print(f"Maior valor: {maior_valor(x, y)}")

if __name__ == "__main__":
    main()
