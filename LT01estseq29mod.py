'''
Receba o tipo de investimento (1 = poupança e 2  = renda  fixa) e o valor do 
investimento.  Calcule  e  mostre  o  valor  corrigido  em  30  dias  sabendo  que  a 
poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados. 
'''

def valor_corrigido(tipo, valor):
    if tipo == 1:
        return valor * 1.03
    elif tipo == 2:
        return valor * 1.05
    else:
        return None

def main():
    tipo = int(input("Tipo de investimento (1=poupança, 2=renda fixa): "))
    valor = float(input("Valor do investimento: "))
    resultado = valor_corrigido(tipo, valor)
    if resultado is not None:
        print(f"Valor corrigido em 30 dias: R$ {resultado:.2f}")
    else:
        print("Tipo de investimento não considerado.")

if __name__ == "__main__":
    main()
