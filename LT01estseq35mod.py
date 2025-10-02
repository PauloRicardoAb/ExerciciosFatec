'''
Receba  2  números  inteiros,  verifique  qual  o  maior  entre  eles.  Calcule  e 
mostre o resultado da somatória dos números ímpares entre esses valores. 
'''

def soma_impares(a, b):
    menor, maior = min(a, b), max(a, b)
    return sum(x for x in range(menor, maior+1) if x % 2 != 0)

def main():
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    print(f"Soma dos ímpares: {soma_impares(x, y)}")

if __name__ == "__main__":
    main()
