'''
Mostre todas as possibilidades de 2 dados de forma que a soma tenha como 
resultado 7.
'''

def possibilidades_soma_7():
    return [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7) if d1 + d2 == 7]

def main():
    for d1, d2 in possibilidades_soma_7():
        print(f"Dado 1: {d1}, Dado 2: {d2}")

if __name__ == "__main__":
    main()
