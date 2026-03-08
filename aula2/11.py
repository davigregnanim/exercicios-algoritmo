# Faça um programa que leia a idade e a categoria de um jogador de futebol (juvenil, adulto, veterano) e calcule a sua
# classificação no time.

idade = int(input("Digite sua idade: "))

if idade < 16:
    print(f"Sua categoria é Juvenil")
elif idade < 30:
    print(f"Sua categoria é Profissional")
else:
    print(f"Sua categoria é Veterano")