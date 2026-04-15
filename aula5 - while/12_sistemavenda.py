# O Sistema define um estoque inicial de produtos e a cada venda, retira quantidade do estoque. O sistema encerra quando não permite vender mais do que o disponível.

estoque = 30

while True:
    qtd = int(input("Olá, quantos produtos você deseja comprar? "))

    if qtd <= 0:
        print("Número inválido!")

    elif qtd > estoque:
        print("Não temos essa quantidade disponível no momento!")
        break

    else:
        estoque -= qtd

        if estoque == 0:
            print("Essa foi nossa última unidade disponível no momento, obrigado por comprar conosco!")
            break
