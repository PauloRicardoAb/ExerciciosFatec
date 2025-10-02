'''
Receba um número inteiro. Calcule e mostre o seu fatorial.
'''

def fatorial(n):
    if n < 0:
        return None
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

def main():
    num = int(input("Digite um número inteiro: "))
    fat = fatorial(num)
    if fat is not None:
        print(f"Fatorial de {num} = {fat}")
    else:
        print("Fatorial não definido para negativos.")

if __name__ == "__main__":
    main()
