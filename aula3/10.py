# O usuário escolhe uma forma de pagamento e o programa informa se há desconto ou acréscimo.

pagamento = input("Qual vai ser a forma de pagamento? (crédito, débito, pix, dinheiro): ").lower()

match pagamento:
    case "crédito":
        print("Há acréscimo de 5% nessa forma de pagamento")
    case "débito":
        print("Há desconto de 5% nessa forma de pagamento")
    case "pix":
        print("Há desconto de 10% nessa forma de pagamento")
    case "dinheiro":
        print("Há desconto de 15% nessa forma de pagamento")
    case _:
        print("Essa forma de pagamento é inválida.")