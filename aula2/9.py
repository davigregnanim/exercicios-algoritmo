# Solicite o preço de um produto e aplique um desconto de 10% se o preço for maior que R$ 100. Exiba o valor final.

preco = float(input("Digite o preço do produto: "))

desconto = preco * (10 / 100)
vf = preco - desconto

if preco > 100:
    print(f"O valor do seu produto aplicado R${vf}")
else:
    print(f"O valor do seu produto continua sendo R${preco}")