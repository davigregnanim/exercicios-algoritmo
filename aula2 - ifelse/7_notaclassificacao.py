# Receba a nota de um aluno e classifique-a como A (90-100), B (80-89), C (70-79), D (60-69), ou F (menos de 60).

nota = int(input("Digite a nota do aluno (0 - 100): "))

if nota < 60:
    print(f"Classificação: F")
elif nota <= 69:
    print(f"Classificação: D")
elif nota <= 79:
    print(f"Classificação: C")
elif nota <= 89:
    print(f"Classificação: B")
else:
    print(f"Classificação: A")