# A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo
# que o carro custa R$90,00 por dia e R$0,20 por KM rodado.

qtdpercorrida = float(input("Digite a quantidade de KM percorridos: "))
qtddias = float(input("Digite a quantidade de dias em que o carro foi alugado: "))

precototal = (qtddias * 90) + (qtdpercorrida * 0.20)

print(f"O preço total a pagar será de R${precototal:.2f}")