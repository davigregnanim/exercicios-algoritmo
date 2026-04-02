# Solicite ao usuário um número e verifique se ele é par ou ímpar.
# Se o número for par, divida-o por 2 e exiba o resultado.
# Se o número for ímpar, multiplique-o por 3 e exiba o resultado.

for i in range(1):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        par = num / 2
        print(f"{par:.2f}")
    else:
        impar = num * 3
        print(f"{impar:.2f}")
