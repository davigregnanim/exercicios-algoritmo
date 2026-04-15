# Faça um controle de estoque com menu de entrada, saída e exibição.

estoque = 0

while True:
    print("CONTROLE DE ESTOQUE")
    print("1 - Entrada de produto")
    print("2 - Saída de produto")
    print("3 - Exibir estoque")
    print("0 - Sair")
    print("")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        adicionar = int(input("Digite a quantidade a adicionar no estoque: "))
        if adicionar > 0:
            estoque += adicionar
            print("Quantidade adicionada com sucesso ao estoque.")
            print("")
        else:
            print("Digite um número válido!")
            print("")

    elif opcao == 2:
        if estoque == 0:
            print("Você ainda não adicionou nenhum produto no estoque!")
            print("")
        else:
            remover = int(input("Digite a quantidade a retirar: "))
            if remover > estoque or remover < 0:
                print("Não há a quantidade necessária para retirar!")
                print("")
            else:
                estoque -= remover
                print("Quantidade retirada com sucesso do estoque.")
                print("")

    elif opcao == 3:
        print(f"Estoque atual: {estoque}")
        print("")

    elif opcao == 0:
        break

print("Programa encerrado com sucesso!")

