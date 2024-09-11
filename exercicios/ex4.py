from expressoes import *

num = int(input("Digite a quantidade de números a ser digitados: "))

lista = [int(input(f"Digite o {i}º número: ")) for i in range(1, num + 1)]


print(f"O MMC dos números é: {mmc_lista(lista)}")