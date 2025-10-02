'''
Receba  3  valores  obrigatoriamente  em  ordem  crescente  e  um  4º  valor  não 
necessariamente em ordem. Mostre os 4 números em ordem crescente. 
'''

def ordenar_quatro(a, b, c, d):
    return sorted([a, b, c, d])

def main():
    v1 = float(input("1º valor (ordem crescente): "))
    v2 = float(input("2º valor (ordem crescente): "))
    v3 = float(input("3º valor (ordem crescente): "))
    v4 = float(input("4º valor: "))
    ordem = ordenar_quatro(v1, v2, v3, v4)
    print("Ordem crescente:", ordem)

if __name__ == "__main__":
    main()
