# Peça um número ao usuário e exiba os múltiplos desse número de 1 a 10.

num = int(input("Digite um número: "))

for i in range(1, 10+1):
    print(f"{num} x {i} = {num * i}")