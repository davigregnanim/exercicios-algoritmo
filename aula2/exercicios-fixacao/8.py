# Pergunte o mês (1-12) e mostre a estação correspondente.

mes = int(input("Digite o mês (1-12): "))

if mes == 12 or mes == 1 or mes == 2 or mes == 3:
    print("Verão")
elif mes == 4 or mes == 5 or mes == 6:
    print("Outono")
elif mes == 7 or mes == 8 or mes == 9:
    print("Inverno")
else:
    print("Primavera")