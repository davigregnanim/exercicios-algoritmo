# Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero.

positivo = 0
negativo = 0
zero = 0

for i in range(10):
    num = int(input("Digite um número: "))

    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else:
        zero += 1

print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Quantidade de zeros: {zero}")