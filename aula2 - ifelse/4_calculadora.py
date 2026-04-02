# Crie uma calculadora simples que permita ao usuário escolher uma operação (adição, subtração, multiplicação ou divisão)
# e dois números, e então exiba o resultado.

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

operacao = input("Selecione uma operação para fazer a conta: (+, -, x, /): ")
if operacao == "+":
    print(f"{num1+num2}")
elif operacao == "-":
    print(f"{num1-num2}")
elif operacao == "x":
    print(f"{num1*num2}")
elif operacao == "/":
    print(f"{num1/num2}")
else:
    print("Digite uma operação válida e tente novamente!")