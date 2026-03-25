# Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5.

N = int(input("Digite um número máximo: "))
multiplo = 0

for i in range(1, N+1):
    if i % 3 == 0 or i % 5 == 0:
        multiplo += 1

print(f"Existem {multiplo} números múltiplos de 3 ou 5")