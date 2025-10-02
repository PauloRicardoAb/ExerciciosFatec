'''
Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
'''

n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))

if (n1 > n2):
    print(F'A diferença entre os numeros é: ', n1 - n2)

else:
    print(F'A diferença entre os numeros é: ', n2 - n1)
