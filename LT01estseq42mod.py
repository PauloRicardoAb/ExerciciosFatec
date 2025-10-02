'''
Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99 
'''

def serie_42():
    return sum(i/(2*i-1) for i in range(1, 51))

def main():
    s = serie_42()
    print(f"Soma da série: {s:.6f}")

if __name__ == "__main__":
    main()
