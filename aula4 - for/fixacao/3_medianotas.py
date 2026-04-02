# Faça um programa que solicite 5 notas e calcule a média.

soma = 0
for i in range(1, 5+1):
    nota = float(input(f"Digite a nota {i}: "))
    soma = soma + nota

media = soma / 5
print(f"A média das notas é {media:.2f}")
