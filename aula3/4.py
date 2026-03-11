# O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis), e o programa exibirá o
# percentual de desconto correspondente.

produto = input("Digite o tipo do produto que você quer ver o desconto: (eletronico, roupas, alimentos, moveis): ").lower()

match produto:
    case "eletronico":
        preco = float(input("Digite o valor do produto: "))
        print(f"O percentual de desconto é 20%, o valor final do produto vai ser de: {preco - preco * (20 / 100)}")
    case "roupas":
        preco = float(input("Digite o valor do produto: "))
        print(f"O percentual de desconto é 15%, o valor final do produto vai ser de: {preco - preco * (15 / 100)}")
    case "alimentos":
        preco = float(input("Digite o valor do produto: "))
        print(f"O percentual de desconto é 10%, o valor final do produto vai ser de: {preco - preco * (10 / 100)}")
    case "moveis":
        preco = float(input("Digite o valor do produto: "))
        print(f"O percentual de desconto é 20%, o valor final do produto vai ser de: {preco - preco * (20 / 100)}")