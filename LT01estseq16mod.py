'''
Receba  a  quantidade  de  horas  trabalhadas,  o  valor  por  hora,  o  percentual 
de  desconto  e  o  número  de  dependentes.  Calcule  o  salário  que  serão  as 
horas  trabalhadas  x  o  valor  por  hora.  Calcule  o  salário  líquido  (=  Salário 
Bruto  –  desconto).  A  cada  dependente  será  acrescido  R$  100  no  Salário 
Líquido. Exiba o salário a receber. 
'''

def calcular_salario(horas_trabalhadas, valor_hora, percentual_desconto, dependentes):
    salario_bruto = horas_trabalhadas * valor_hora
    desconto = salario_bruto * (percentual_desconto / 100)
    salario_liquido = salario_bruto - desconto
    salario_liquido += dependentes * 100
    return salario_liquido

def main():
    horas = float(input("Horas trabalhadas: "))
    valor = float(input("Valor por hora: "))
    desconto = float(input("Percentual de desconto: "))
    dependentes = int(input("Número de dependentes: "))
    salario = calcular_salario(horas, valor, desconto, dependentes)
    print(f"Salário a receber: R$ {salario:.2f}")

if __name__ == "__main__":
    main()
