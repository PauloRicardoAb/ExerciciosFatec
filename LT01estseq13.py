# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias
# durará esse alimento sabendo que a pessoa consome 50g ao dia.


alimento_kg = float(input("Quantidade de alimento (kg): "))
        
dias = (alimento_kg * 1000) // 50
print(f"O alimento durará {int(dias)} dias.")
