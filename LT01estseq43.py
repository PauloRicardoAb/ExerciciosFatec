'''
Calcule e mostre quantos anos serão necessários para que Ana seja maior que 
Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m 
e cresce 2 cm ao ano.
'''

# Dados iniciais
altura_ana = 110  # 1,10 m = 110 cm
altura_maria = 150  # 1,5 m = 150 cm
crescimento_ana = 3  # 3 cm por ano
crescimento_maria = 2  # 2 cm por ano

anos = 0

print("Evolução das alturas:")
print(f"Ano {anos}: Ana = {altura_ana} cm, Maria = {altura_maria} cm")

# Simula o crescimento ano a ano
while altura_ana <= altura_maria:
    anos += 1
    altura_ana += crescimento_ana
    altura_maria += crescimento_maria
    print(f"Ano {anos}: Ana = {altura_ana} cm, Maria = {altura_maria} cm")

print(f"\nAna será maior que Maria após {anos} anos.")
print(f"Neste momento, Ana terá {altura_ana} cm e Maria terá {altura_maria} cm.")