# Solicite um número ao usuário e exiba o seu fatorial (n!).

num = int(input("Digite um número: "))
total = 1

for i in range(num, 0, -1):
    total =  total * i

print(total)