'''
Receba  o  número  da  base  e  do  expoente.  Calcule  e  mostre  o  valor  da 
potência.
'''

def potencia(base, expoente):
    return base ** expoente

def main():
    base = float(input("Base: "))
    exp = int(input("Expoente: "))
    print(f"{base}^{exp} = {potencia(base, exp)}")

if __name__ == "__main__":
    main()
