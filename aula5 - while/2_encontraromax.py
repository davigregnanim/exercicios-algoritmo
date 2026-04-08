# Crie um programa que peça ao usuário para inserir números e encontre o maior número inserido. O programa deve continuar
# pedindo números até que o usuário digite "sair".

entrada = input("Digite um número: ")

if entrada != "sair":
    maior = int(entrada)

    while True:
        entrada = input("Digite outro número (ou 'sair'): ")

        if entrada == "sair":
            break

        num = int(entrada)

        if num > maior:
            maior = num

    print(maior)
else:
    print("Nenhum número foi digitado!")