# O usuário escolhe um destino (São Paulo, Rio de Janeiro, Curitiba, Salvador) e recebe o valor da passagem.

print("1 - São Paulo")
print("2 - Rio de Janeiro")
print("3 - Curitiba")
print("4 - Salvador")
destino = input("Qual destino você deseja ir? ")

match destino:
    case "1":
        print("O valor da passagem é de R$80,00")
    case "2":
        print("O valor da passagem é de R$220,00")
    case "3":
        print("O valor da passagem é de R$300,00")
    case "4":
        print("O valor da passagem é de R$380,00")