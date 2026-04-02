# Crie um programa que solicite ao usuário um número e informe se ele é primo ou não. Lembre-se de que um número primo é
# aquele que é divisível apenas por 1 e por ele mesmo.

num = int(input("Digite um número para verificar se é primo: "))
primo = True

for i in range(1, num):
    if num % i == 0:
        primo = False

if primo and num > 1:
    print("Primo")
else:
    print("Não é primo")