# Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

passo = int(input("Digite o número da tabuada que você deseja ver: "))

for i in range(1, 11):
    print(f"{i} x {passo} = {i * passo}")

# versão anterior (raciocinio maluco)
# for i in range(0, passo*10+1, +passo):
#    print(f"{i/passo:.0f} x {passo} = {(i/passo)*passo:.0f}")
