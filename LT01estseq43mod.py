'''
Calcule e mostre quantos anos serão necessários para que Ana seja maior que 
Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m 
e cresce 2 cm ao ano.
'''

def anos_ana_maior():
    ana = 110
    maria = 150
    anos = 0
    while ana <= maria:
        ana += 3
        maria += 2
        anos += 1
    return anos, ana, maria

def main():
    anos, ana, maria = anos_ana_maior()
    print(f"Ana será maior que Maria em {anos} anos.")
    print(f"Altura Ana: {ana} cm, Altura Maria: {maria} cm")

if __name__ == "__main__":
    main()
