horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))
num_dependentes = int(input("Digite o número de dependentes: "))

salario_bruto = horas_trabalhadas * valor_hora

desconto = salario_bruto * (percentual_desconto / 100)

salario_liquido = salario_bruto - desconto

salario_liquido += num_dependentes * 100

print(f"Salário a receber: R$ {salario_liquido:.2f}")