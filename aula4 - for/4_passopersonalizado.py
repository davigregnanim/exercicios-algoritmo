# Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente.

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
passo = int(input("Digite o passo: "))

if passo == 0:
    print("O passo tem que ser diferente de 0!")
else:
    if passo > 0:
        for i in range(inicio, fim+1, passo):
            print(i)
    else:
        for i in range(inicio, fim-1, passo):
            print(i)