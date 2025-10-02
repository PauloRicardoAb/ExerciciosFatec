'''
Receba  3  valores  obrigatoriamente  em  ordem  crescente  e  um  4º  valor  não 
necessariamente em ordem. Mostre os 4 números em ordem crescente
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if valor2 < valor1:
    print("Digite os valores em ordem crescente")
    pass
valor3 = int(input("Digite o terceiro valor: "))
if valor3 < valor2:
    print("Digite os valores em ordem crescente")
    pass
valor4 = int(input("Digite o quarto valor: "))

if valor4 > valor3:
    print(valor1, valor2, valor3, valor4)
elif valor4 > valor2:
    print(valor1, valor2, valor4, valor3)
elif valor4 > valor1:
    print(valor1, valor4, valor2, valor3)
elif valor4 < valor1:
    print(valor4, valor1, valor2, valor3)