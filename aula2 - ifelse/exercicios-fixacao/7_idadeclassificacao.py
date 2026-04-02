# Solicite a idade e classifique: criança, adolescente, adulto ou idoso.

idade = int(input("Digite sua idade: "))

if idade > 65:
    print("Classificação: Idoso")
elif idade > 18:
    print("Classificação: Adulto")
elif idade > 13:
    print("Classificação: Adolescente")
else:
    print("Classificação: Criança")