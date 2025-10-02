'''
Calcule  a  quantidade  de  litros  gastos  em  uma  viagem,  sabendo  que  o 
automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. 
'''

def calcular_litros_gastos(tempo_horas, velocidade_media):
    distancia = tempo_horas * velocidade_media
    litros = distancia / 12
    return litros

def main():
    tempo = float(input("Tempo de percurso (horas): "))
    velocidade = float(input("Velocidade média (km/h): "))
    litros = calcular_litros_gastos(tempo, velocidade)
    print(f"Litros gastos na viagem: {litros:.2f}")

if __name__ == "__main__":
    main()
