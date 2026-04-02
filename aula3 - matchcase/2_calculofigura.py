# Desenvolva um programa que permita ao usuário escolher entre calcular a área de um quadrado, retângulo
# ou triângulo einsira os valores necessários para o cálculo.

figura = input("Você quer calcular a área de qual figura geométrica? (quadrado, retangulo ou triangulo): ").lower()

match figura:
    case "quadrado":
        n1 = float(input("Digite o valor do lado do quadrado: "))
        print(f"Base² = {n1 * n1}")
    case "retangulo":
        n1 = float(input("Digite o valor da base do retangulo: "))
        n2 = float(input("Digite o valor da altura do retangulo: "))
        print(f"Base x Altura = {n1 * n2}")
    case "triangulo":
        n1 = float(input("Digite o valor da base do triangulo: "))
        n2 = float(input("Digite o valor da altura do triangulo: "))
        print(f"Base x Altura / 2 = {(n1 * n2) / 2}")
    case _:
        print("Escreva uma moeda válida!")


