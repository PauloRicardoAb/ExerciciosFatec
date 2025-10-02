'''
Receba  2  números  inteiros.  Verifique  e  mostre  todos  os  números  primos 
existentes entre eles
'''

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primos_entre(a, b):
    menor, maior = min(a, b), max(a, b)
    return [x for x in range(menor, maior+1) if eh_primo(x)]

def main():
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    primos = primos_entre(x, y)
    print("Primos:", primos)

if __name__ == "__main__":
    main()
