'''
Calcule  a  quantidade  de  litros  gastos  em  uma  viagem,  sabendo  que  o 
automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. 
'''

tempo = float(input("Digite o tempo de percurso (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))

distancia = tempo * velocidade_media

litros_gastos = distancia / 12

print(f"Quantidade de litros gastos na viagem: {litros_gastos:.2f} litros")