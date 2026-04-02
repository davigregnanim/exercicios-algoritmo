# Implemente um conversor de moedas que permita ao usuário escolher entre Dólar (USD), Euro (EUR) e Libra (GBP) e
# converter um valor informado para Reais (BRL).

moeda = input("Escreva uma moeda para converter para reais (dólar, euro, libra): ").lower()

match moeda:
    case "dólar":
        n1 = float(input("Digite o valor que você quer converter: "))
        print(f"A conversão dá R${n1 / 5.20:.2f}")
    case "euro":
        n1 = float(input("Digite o valor que você quer converter: "))
        print(f"A conversão dá R${n1 / 6.03:.2f}")
    case "libras":
        n1 = float(input("Digite o valor que você quer converter: "))
        print(f"A conversão dá R${n1 / 6.98:.2f}")
    case _:
        print("Escreva uma moeda válida!")


