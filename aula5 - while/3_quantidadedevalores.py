# Conte quantos valores positivos, negativos e zeros foram digitados.

positivo = 0
negativo = 0
zero = 0

while True:
    entrada = input("Digite outro número número: (ou 'sair'): ")

    if entrada == "sair":
        break

    num = int(entrada)
    
    if num == 0:
        zero = zero + 1
    elif num > 0:
        positivo = positivo + 1
    else:
        negativo = negativo + 1

print(f"Há {positivo} números positivos, {negativo} números negativos e {zero} números zeros.")