'''
Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
'''

def serie_45():
    s = 0
    for i in range(1, 16):
        termo = i / (i*i)
        if i % 2 == 0:
            s -= termo
        else:
            s += termo
    return s

def main():
    print(f"Soma da série: {serie_45():.6f}")

if __name__ == "__main__":
    main()
