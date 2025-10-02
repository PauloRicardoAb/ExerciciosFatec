'''
Receba o número de voltas, a extensão do circuito (em metros) e o tempo de 
duração (minutos). Calcule e mostre a velocidade média em km/h. 
'''

# Entrada de dados
voltas = int(input("Digite o número de voltas: "))
extensao_metros = float(input("Digite a extensão do circuito em metros: "))
tempo_minutos = float(input("Digite o tempo de duração em minutos: "))

# Cálculo da distância total percorrida em km
distancia_total_km = (voltas * extensao_metros) / 1000

# Conversão do tempo para horas
tempo_horas = tempo_minutos / 60

# Cálculo da velocidade média em km/h
velocidade_media = distancia_total_km / tempo_horas

# Exibição do resultado
print(f"Velocidade média: {velocidade_media:.2f} km/h")