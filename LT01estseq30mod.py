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

def calcular_idade(dn, mn, an, da, ma, aa):
    anos = aa - an
    meses = ma - mn
    dias = da - dn
    if dias < 0:
        meses -= 1
        mes_anterior = ma - 1 if ma > 1 else 12
        ano_anterior = aa if ma > 1 else aa - 1
        dias += dias_no_mes(mes_anterior, ano_anterior)
    if meses < 0:
        anos -= 1
        meses += 12
    return anos, meses, dias

def main():
    dn = int(input("Dia nascimento: "))
    mn = int(input("Mês nascimento: "))
    an = int(input("Ano nascimento: "))
    da = int(input("Dia atual: "))
    ma = int(input("Mês atual: "))
    aa = int(input("Ano atual: "))
    anos, meses, dias = calcular_idade(dn, mn, an, da, ma, aa)
    print(f"Idade: {anos} anos, {meses} meses, {dias} dias")

if __name__ == "__main__":
    main()
