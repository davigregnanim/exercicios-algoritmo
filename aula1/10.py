# Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos"

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 % n2 == 0 or n2 % n1 == 0:
    print(f"Os números {n1} e {n2} são múltiplos")
else:
    print(f"Os números {n1} e {n2} não são múltiplos")