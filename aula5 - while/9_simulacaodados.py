# Crie um programa que simule a leitura de dados de um sensor e continue capturando dados até que um valor fora do intervalo
# de operação seja detectado (por exemplo, fora de 0 a 100)

while True:
    num = int(input("Digite um número: "))
    if num < 0 or num > 100:
        print("Bep! Fora do intervalo!")
        break