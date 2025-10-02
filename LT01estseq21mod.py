'''
Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. 
Mostre a mensagem de acordo com a média: 
a. Se a média for >= 6,0 exibir “APROVADO”; 
b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”; 
c. Se a média for < 3,0 exibir “RETIDO”. 
'''

def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao_aluno(media):
    if media >= 6.0:
        return "APROVADO"
    elif media >= 3.0:
        return "EXAME"
    else:
        return "RETIDO"

def main():
    notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
    media = calcular_media(notas)
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao_aluno(media)}")

if __name__ == "__main__":
    main()
