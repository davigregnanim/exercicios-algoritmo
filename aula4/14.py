# Peça ao usuário para digitar 5 números e exiba o maior e o menor deles.

maior = 0
menor = 0

for i in range(1, 6):
    num = int(input("Digite o número: "))

    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")

