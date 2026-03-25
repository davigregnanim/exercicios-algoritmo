# Peça 5 notas ao usuário e calcule a média delas.

nota = 0
for i in range(1, 6):
    nota_atual = float(input("Digite a nota: "))
    nota += nota_atual

print(f"A médias das notas é {nota/5:.2f}")