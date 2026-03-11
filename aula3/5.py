# vO usuário informa uma cor em português (vermelho, azul, verde, amarelo), e o
# programa exibe sua tradução para inglês.

cor = input("Digite uma cor em português para traduzir em inglês: ").lower()

match cor:
    case "vermelho":
        print("Red")
    case "azul":
        print("Blue")
    case "amarelo":
        print("Yellow")