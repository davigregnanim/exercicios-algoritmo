# Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele
# trabalha 8 horas por dia e ganha R$25,00 por hora trabalhada.

diastrabalhados = float(input("Digite a quantidade de dias em que você trabalhou: "))

salario = 200 * diastrabalhados

print(f"O seu salário será de R${salario:.2f}")