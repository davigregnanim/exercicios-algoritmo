# Peça um número ao usuário e some separadamente os pares e os ímpares de 1 até esse número.

# pedir um numero = 25

# somar separadamente os pares e impares de 1 -> 25
# 1 3 5 7 9 11 13 15 17 19 21 23 25
# 2 4 6 8 10 12 14 16

num = int(input("Digite um número: "))
par = 0
impar = 0

for i in range(1, num+1):
    if i % 2 == 0:
        par += i
    else:
        impar += i

print(f"Soma dos números pares: {par}")
print(f"Soma dos números ímpares: {impar}")

