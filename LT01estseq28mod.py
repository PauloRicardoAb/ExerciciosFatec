'''
Receba  o  preço  atual  e  a  média  mensal  de  um  produto.  Calcule  e  mostre  o 
novo preço sabendo que: 
Venda Mensal Preço Atual Preço Novo 
< 500 < 30 + 10% 
>= 500 e < 1000 >= 30 e < 80 +15% 
>= 1000 >= 80 - 5% 
Obs.: para outras condições, preço novo será igual ao preço atual.
'''

def calcular_novo_preco(preco_atual, venda_mensal):
    if venda_mensal < 500 and preco_atual < 30:
        return preco_atual * 1.10
    elif 500 <= venda_mensal < 1000 and 30 <= preco_atual < 80:
        return preco_atual * 1.15
    elif venda_mensal >= 1000 and preco_atual >= 80:
        return preco_atual * 0.95
    else:
        return preco_atual

def main():
    preco = float(input("Preço atual: "))
    media = float(input("Média mensal de vendas: "))
    novo = calcular_novo_preco(preco, media)
    print(f"Novo preço: R$ {novo:.2f}")

if __name__ == "__main__":
    main()
