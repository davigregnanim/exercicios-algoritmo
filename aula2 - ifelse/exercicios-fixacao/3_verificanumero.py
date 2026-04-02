# Verifique se um número é positivo, negativo ou zero.

num = float(input("Digite um numero: "))

if num == 0:
    print("O número é igual a 0")
elif num < 0:
    print("O número é negativo")
else:
    print("O número é positivo")