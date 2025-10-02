inicio = int(input("horas de inicio: "))
final = int(input("horas final: "))

if inicio < 24 and final < 24:
    if inicio > fim:
        print("O tempo de jogo é: ", final-inicio)
    else:
        print("O tempo de jogo é: ", inicio-final)