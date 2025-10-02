'''
Calcule e mostre o quadrado dos números entre 10 e 150. 
'''

def quadrados_10_150():
    return [(n, n**2) for n in range(10, 151)]

def main():
    for n, q in quadrados_10_150():
        print(f"{n}^2 = {q}")

if __name__ == "__main__":
    main()
