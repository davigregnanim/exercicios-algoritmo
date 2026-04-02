# O computador escolhe um número aleatório de 1 a 10, e o usuário tem 3 tentativas para adivinhar. Dê dicas se o número é maior ou menor.

num_aleatorio = 2

for i in range(1, 4):
    num = int(input(f"Tentativa {i}/3 - Digite um número: "))
    if num > num_aleatorio:
        print("Seu número atual é maior que o número aleatório.")
    elif num < num_aleatorio:
        print("Seu número atual é menor que o número aleatório.")
    else:
        print("Parabéns, você acertou o número aleatório!")
        break

