# Classifique a nota de um aluno (A, B, C, D, F).

nota = float(input("Digite a nota do aluno: "))

if nota <= 3:
    print("Classificação: F")
elif nota <= 5:
    print("Classificação: D")
elif nota <= 7:
    print("Classificação: C")
elif nota <= 9:
    print("Classificação: B")
else:
    print("Classificação: A")