# Peça ao usuário seu peso e altura, calcule o Índice de Massa Corporal (IMC) e classifique-o como "Abaixo do peso",
# "Peso normal", "Sobrepeso" ou "Obesidade".

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura ** 2

if imc < 18.5:
    print(f"Classificação: Abaixo do Peso")
elif imc < 24.99:
    print(f"Classificação: Peso Normal")
elif imc < 29.99:
    print(f"Classificação: Sobrepeso")
elif imc < 34.99:
    print(f"Classificação: Obesidade Grau 1")
elif imc < 39.99:
    print(f"Classificação: Obesidade Grau 2")
else:
    print(f"Classificação: Obesidade Grau 3")