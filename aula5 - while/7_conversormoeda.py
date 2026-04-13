# Crie um programa que converta uma quantia em dólares para euros. Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0".

while True:
    dolar = float(input("Digite uma quantia em dólar para converter à euro (0 para parar): "))

    if dolar == 0:
        break

    else:
        euro = dolar / 1.16
        print(f"{euro:.2f}")