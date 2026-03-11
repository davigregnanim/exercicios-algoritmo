# O usuário escolhe um produto e o programa informa o preço.

print("1 - Coxinha de frango")
print("2 - Kibe recheado")
print("3 - Esfiha de carne")
print("4 - Empada de palmito")
salgado = input("Escolha um salgado: ")
match salgado:
    case "1":
        print("O preço do salgado é de R$6,50")
    case "2":
        print("O preço do salgado é de R$7,00")
    case "3":
        print("O preço do salgado é de R$6,00")
    case "4":
        print("O preço do salgado é de R$8,00")