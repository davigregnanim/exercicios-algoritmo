# Crie um programa que simule um caixa eletrônico, que continue pedindo ao usuário para inserir um valor de saque até
# que o saldo da conta seja zero ou negativo.

valortotal = 5000

print("SAQUE ELETRÔNICO")
print(f"Saldo atual: R${valortotal}")

valor = int(input("Olá, quanto dinheiro você deseja sacar? "))
while valortotal >= 0:
    if valor <= valortotal:
        valortotal = valortotal - valor
        print("SAQUE ELETRÔNICO")
        print(f"Saldo atual: R${valortotal}")
        valor = int(input("Olá, quanto dinheiro você deseja sacar? "))
    else:
        print("Saldo Indisponível!")
        break