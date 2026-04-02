# Solicite a idade do usuário e informe se ele é menor de idade, maior de idade ou idoso (considerando 18 e 65 anos como limites).

idade = int(input("Digite sua idade: "))

if idade <=17:
    print(f"Você é menor de idade")
elif idade <= 65:
    print(f"Você é maior de idade")
else:
    print(f"Vocé é idoso")