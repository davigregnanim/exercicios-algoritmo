# Peça um número ao usuário e some seus dígitos (exemplo: 123 → 1+2+3 = 6).

num = input("Digite um número: ")
soma = 0

for caractere in num:
    soma += int(caractere)

print(soma)