# Faça um programa que converta uma temperatura de Celsius para Fahrenheit. Continue pedindo ao usuário para inserir uma
# nova temperatura em Celsius até que ele digite "sair".

while True:
    entrada = input("Digite uma temperatura em Celsius (ou 'sair'): ")
    if entrada == "sair":
        break

    celsius = float(entrada)
    fahrenheit = (celsius * 1.8) + 32

    print(f"A conversão para fahrenheit é igual a {fahrenheit}°F")


