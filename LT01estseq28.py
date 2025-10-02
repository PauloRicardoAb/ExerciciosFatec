'''
Receba  o  preço  atual  e  a  média  mensal  de  um  produto.  Calcule  e  mostre  o 
novo preço sabendo que: 
Venda Mensal Preço Atual Preço Novo 
< 500 < 30 + 10% 
>= 500 e < 1000 >= 30 e < 80 +15% 
>= 1000 >= 80 - 5% 
Obs.: para outras condições, preço novo será igual ao preço atual.
'''

# Entrada de dados
preco_atual = float(input("Digite o preço atual do produto: "))
venda_mensal = float(input("Digite a venda mensal do produto: "))

# Cálculo do novo preço baseado nas condições
if venda_mensal < 500 and preco_atual < 30:
    novo_preco = preco_atual * 1.10  # +10%
elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30 and preco_atual < 80:
    novo_preco = preco_atual * 1.15  # +15%
elif venda_mensal >= 1000 and preco_atual >= 80:
    novo_preco = preco_atual * 0.95  # -5%
else:
    novo_preco = preco_atual  # Preço atual mantido

# Exibição do resultado
print(f"Preço atual: R$ {preco_atual:.2f}")
print(f"Novo preço: R$ {novo_preco:.2f}")