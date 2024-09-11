from expressoes import *

num = int(input("Digite a quantidade de números a ser digitados no primeiro conjunto: "))
lista_1 = [int(input(f"Digite o {i}º número: ")) for i in range(1, num + 1)]

num = int(input("Digite a quantidade de números a ser digitados no segundo conjunto: "))
lista_2 = [int(input(f"Digite o {i}º número: ")) for i in range(1, num + 1)]

print(f"A união dos conjuntos é {uniao_conjuntos(lista_1, lista_2)}")