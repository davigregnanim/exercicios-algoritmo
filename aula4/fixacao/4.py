#  Crie um contador que peça ao usuário um número inicial, um número final e um incremento e exiba os valores gerados.

inicial = int(input("Digite o número inicial: "))
final = int(input("Digite o número final: "))
incremento = int(input("Digite o incremento: "))
if incremento == 0:
    print("O incremento tem que ser diferente de 0!")
else:
    incremento = abs(incremento)
    if inicial < final:
        for i in range(inicial, final+1, incremento):
            print(i)
    else:
        for i in range(inicial, final-1, -incremento):
            print(i)