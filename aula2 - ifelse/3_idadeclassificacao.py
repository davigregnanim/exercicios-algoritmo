# Peça ao usuário para inserir a idade de uma pessoa e classifique-a como "Criança" (0-12 anos), "Adolescente" (13-17 anos),
# "Adulto" (18-64 anos) ou "Idoso" (65+ anos).

idade = int(input("Digite uma idade: "))

if idade <= 12:
    print(f"Classificação: Criança")
elif idade <= 17:
    print(f"Classificação: Adolescente")
elif idade <= 64:
    print(f"Classificação: Adulto")
else:
    print(f"Classificação: Idoso")