'''
Receba o número de voltas, a extensão do circuito (em metros) e o tempo de 
duração (minutos). Calcule e mostre a velocidade média em km/h. 
'''

def calcular_velocidade_media(voltas, extensao_m, tempo_min):
    distancia_km = (voltas * extensao_m) / 1000
    tempo_h = tempo_min / 60
    if tempo_h == 0:
        return 0
    return distancia_km / tempo_h

def main():
    voltas = int(input("Número de voltas: "))
    extensao = float(input("Extensão do circuito (m): "))
    tempo = float(input("Tempo de duração (min): "))
    vmedia = calcular_velocidade_media(voltas, extensao, tempo)
    print(f"Velocidade média: {vmedia:.2f} km/h")

if __name__ == "__main__":
    main()
