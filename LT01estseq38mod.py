'''
Receba  100  números  inteiros  reais.  Verifique  e  mostre  o  maior  e  o  menor 
valor. Obs.: somente valores positivos.
'''

def maior_menor_positivos(numeros):
    positivos = [x for x in numeros if x > 0]
    return max(positivos), min(positivos)

def main():
    nums = []
    for i in range(1, 101):
        while True:
            n = float(input(f"{i}º número positivo: "))
            if n > 0:
                nums.append(n)
                break
            else:
                print("Apenas positivos!")
    maior, menor = maior_menor_positivos(nums)
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

if __name__ == "__main__":
    main()
