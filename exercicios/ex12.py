from expressoes import *

num = int(input("Digite a quantidade de números a ser digitados no primeiro conjunto: "))
lista_1 = [int(input(f"Digite o {i}º número: ")) for i in range(1, num + 1)]

num = int(input("Digite a quantidade de números a ser digitados no segundo conjunto: "))
lista_2 = [int(input(f"Digite o {i}º número: ")) for i in range(1, num + 1)]


sub, caso = subconjunto(lista_1, lista_2)


if caso:
    print(f"É subconjunto!")
    print(f"O subconjunto dos conjuntos é: {sub}")
else:
    print(f"Não é subconjunto!")