alimento_kg = float(input("Quantidade de alimento (kg): "))
        
dias = (alimento_kg * 1000) // 50
print(f"O alimento durará {int(dias)} dias.")
