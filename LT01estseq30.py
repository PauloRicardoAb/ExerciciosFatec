'''
Receba  a  data  de  nascimento  e  atual  em  ano,  mês  e  dia.  Calcule  e  mostre  a 
idade em anos, meses e dias, considerando os anos bissextos. 
'''

def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_no_mes(mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if eh_bissexto(ano) else 28

# Entrada de dados
print("Data de nascimento:")
dia_nasc = int(input("Dia: "))
mes_nasc = int(input("Mês: "))
ano_nasc = int(input("Ano: "))

print("\nData atual:")
dia_atual = int(input("Dia: "))
mes_atual = int(input("Mês: "))
ano_atual = int(input("Ano: "))

# Cálculo da idade
anos = ano_atual - ano_nasc
meses = mes_atual - mes_nasc
dias = dia_atual - dia_nasc

# Ajustes quando os dias são negativos
if dias < 0:
    meses -= 1
    mes_anterior = mes_atual - 1 if mes_atual > 1 else 12
    ano_anterior = ano_atual if mes_atual > 1 else ano_atual - 1
    dias += dias_no_mes(mes_anterior, ano_anterior)

# Ajustes quando os meses são negativos
if meses < 0:
    anos -= 1
    meses += 12

print(f"\nIdade: {anos} anos, {meses} meses e {dias} dias")