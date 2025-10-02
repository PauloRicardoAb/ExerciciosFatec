'''
Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem 
crescente.
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    print(valor2, valor1)
elif valor1 < valor2:
    print(valor1, valor2)    
else:
    print("Regra de negocio incorreta.")

    