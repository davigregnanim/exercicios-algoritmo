# Peça um número ao usuário e exiba sua tabuada de 1 a 10, mas se for múltiplo de 3, substitua pelo texto "Multiplo de 3".

num = int(input("Digite um número para ver a sua tabuada: "))

for i in range(1, 11):

    total = num * i

    if total % 3 == 0:
        print(f"{num} x {i} = Multiplo de 3")
    else:
        print(f"{num} x {i} = {total}")