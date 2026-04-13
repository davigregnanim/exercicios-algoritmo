#  Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) e calcule a média dessas notas. O programa
#  deve parar quando o usuário digitar uma nota negativa.

notatotal = 0
loop = 0

while True:
    notaatual = int(input("Digite uma nota (número negativo para finalizar): "))

    if notaatual >= 0:
        notatotal += notaatual
        loop += 1
    else:
        break

if loop > 0:
    print(notatotal / loop)
else:
    print("Não é possivel dividir por zero.")
