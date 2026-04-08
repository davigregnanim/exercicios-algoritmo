# Crie um programa que solicite ao usuário para inserir números e some esses números até que o usuário insira zero.
# Quando zero for inserido, o programa deve imprimir a soma total.

soma = 0
num = int(input("Digite um número: "))

while num != 0:
    soma = soma + num
    num = int(input("Digite outro número (0 para sair): "))

print(soma)

