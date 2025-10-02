'''
Receba  um  número  inteiro.  Calcule  e  mostre  a  série  de  Fibonacci  até  o  seu 
N’nésimo termo.
'''

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def main():
    n = int(input("Digite N: "))
    seq = fibonacci(n)
    print("Fibonacci:", ", ".join(str(x) for x in seq))

if __name__ == "__main__":
    main()
