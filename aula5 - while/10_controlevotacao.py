# Faça um programa que permita cadastrar votos para 3 candidatos. Exibe contagem ao final quando for digitado "fim".

candidato1 = 0
candidato2 = 0
candidato3 = 0

while True:
    print("CONTROLE ELEITORAL")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("")


    opcao = input("Digite o número do candidato que você deseja cadastrar o voto ('fim' para finalizar e mostrar resultados): ").lower()

    if opcao == "fim":
        print(f"Candidato 1: {candidato1}")
        print(f"Candidato 2: {candidato2}")
        print(f"Candidato 3: {candidato3}")
        break
    
    else:
        opcao = int(opcao)

        if opcao == 1:
            candidato1 += 1

        elif opcao == 2:
            candidato2 += 1

        elif opcao == 3:
            candidato3 += 1

