# O usuário digita o preço e a quantidade de produtos até digitar “sair”. O Sistema mostra a quantidade de produtos e o valor final da compra.

preco = 0
produtos = 0
total = 0

while True:
    valor = input("Digite o preço do produto: ")

    if valor == "sair":
        print(f"Quantidade de produtos comprados: {produtos}")
        print(f"Total gasto: R${total}")
        break

    else:
        qtd = input("Digite a quantidade: ")
        valor = float(valor)
        qtd = int(qtd)

        total += valor * qtd

        produtos += 1