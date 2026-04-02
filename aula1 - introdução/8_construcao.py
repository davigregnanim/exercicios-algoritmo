# Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de
# tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite o valor da altura da parede: "))

area = largura * altura
qtd_tinta = area/2

print(f"A área da parede: {area}")
print(f"Quantidade de tinta necessária: {qtd_tinta:.1f} litros")