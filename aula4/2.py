# Peça ao usuário um número e exiba uma contagem de 1 até esse número.

num = int(input("Digite um número para contar de 1 até ele: "))

for num in range(1, num+1, +1):
    print(num)