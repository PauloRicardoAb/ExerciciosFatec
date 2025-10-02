'''
Calcule  a  quantidade  de  grãos  contidos  em  um  tabuleiro  de  xadrez  onde: 
Casa:  1 2 3 4 ...  64 
Qdte:  1 2 4 8 ...  N
'''

def graos_tabuleiro():
    return sum(2**(i-1) for i in range(1, 65))

def main():
    total = graos_tabuleiro()
    print(f"Total de grãos: {total}")

if __name__ == "__main__":
    main()
