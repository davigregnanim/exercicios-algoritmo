# Receba o peso e altura e calcule o IMC, mostrando a classificação.

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