valorUm = int(input("Digite o primeiro valor: "))
valorDois = int(input("Digite o segundo valor: "))

if valorUm > valorDois:
    if valorUm % valorDois == 0:
        print("O primeiro valor é multiplo pelo segundo")
    else:
        print("O primeiro valor não é multiplo pelo segundo")
elif valorUm < valorDois:
    if valorDois % valorUm == 0:
        print("O Segundo valor é multiplo pelo primeiro")
    else:
        print("O segundo valor não é multiplo pelo primeiro")