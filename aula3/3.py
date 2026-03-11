# O programa deve pedir ao usuário que informe seu nome de usuário e, com base nisso, conceder
# um nível de acesso

usuario = input("Digite o usuário (admin, professor, aluno): ").lower()

match usuario:
    case "admin":
        print("Acesso total")
    case "professor":
        print("Acesso ao ambiente acadêmico")
    case "aluno":
        print("Acesso ao ambiente de estudos")
    case _:
        print("Usuário não encontrado")