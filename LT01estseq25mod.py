'''
Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do 
jogo  em  horas  e  minutos,  sabendo  que  o  tempo  máximo  é  menor  que  24 
horas e pode começar num dia e terminar noutro.
'''

def calcular_tempo_jogo(hora_ini, min_ini, hora_fim, min_fim):
    ini = hora_ini * 60 + min_ini
    fim = hora_fim * 60 + min_fim
    if fim < ini:
        fim += 24 * 60
    duracao = fim - ini
    horas = duracao // 60
    minutos = duracao % 60
    return horas, minutos

def main():
    hi = int(input("Hora início: "))
    mi = int(input("Minuto início: "))
    hf = int(input("Hora final: "))
    mf = int(input("Minuto final: "))
    h, m = calcular_tempo_jogo(hi, mi, hf, mf)
    print(f"Duração do jogo: {h} horas e {m} minutos")

if __name__ == "__main__":
    main()
