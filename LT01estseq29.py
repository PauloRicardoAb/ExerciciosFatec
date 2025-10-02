'''
Receba o tipo de investimento (1 = poupança e 2  = renda  fixa) e o valor do 
investimento.  Calcule  e  mostre  o  valor  corrigido  em  30  dias  sabendo  que  a 
poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados. 
'''

# Entrada de dados
tipo_investimento = int(input("Digite o tipo de investimento (1 = poupança, 2 = renda fixa): "))
valor_investimento = float(input("Digite o valor do investimento: "))

# Cálculo do valor corrigido baseado no tipo
if tipo_investimento == 1:  # Poupança
    valor_corrigido = valor_investimento * 1.03  # 3%
    print(f"Valor corrigido em 30 dias (poupança): R$ {valor_corrigido:.2f}")
elif tipo_investimento == 2:  # Renda fixa
    valor_corrigido = valor_investimento * 1.05  # 5%
    print(f"Valor corrigido em 30 dias (renda fixa): R$ {valor_corrigido:.2f}")
else:
    print("Tipo de investimento não considerado.")