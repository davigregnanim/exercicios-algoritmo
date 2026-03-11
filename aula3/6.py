# O usuário seleciona uma opção de atendimento telefônico

print("\n===== CAIXA ELETRÔNICO =====")
print("1 - Suporte Técnico")
print("2 - Financeiro")
print("3 - Cancelamento")
print("4 - Falar com um atendente")

opcao = int(input("Escolha uma opção: "))
match opcao:
    case "1":
        print("Olá você está no suporte técnico!")
    case "2":
        print("Olá você está no financeiro!")
    case "3":
        print("Olá você quer mesmo fazer o cancelamento?")
    case "4":
        print("Olá você está falando com um atendente!")