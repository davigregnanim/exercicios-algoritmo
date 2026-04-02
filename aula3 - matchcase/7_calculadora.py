# O usuário escolhe uma operação matemática (+, -, *, /) e insere dois números. O programa exibe o resultado.

opcao = input("Escolha uma operação (+, -, *, /): ")
match opcao:
    case "+":
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        print(n1 + n2)
    case "-":
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        print(n1 - n2)
    case "*":
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        print(n1 * n2)
    case "/":
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        print(n1 / n2)