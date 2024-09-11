import math
from functools import reduce
from collections import Counter

def mdc(a,b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    
    return a




def mmc(a,b):
    return abs(a * b) // mdc(a, b)




def mdc_lista(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    return reduce(mdc, lista)




def mmc_lista(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    return reduce(mmc, lista)



def testa_primos():
    primos_list = []
    primo = True
    
    for i in lista:    
        for divisor in range(2,int(n**0.5)+1):
            if n % divisor == 0:
                primo == False
                break
        
        if primo:
            primos_list.append(n)
            primos_counter += 1

    return primos_list, primos_counter



def fatores_primos(n):
        fatores = []
        divisor = 2
        
        while n > 1:
            while n % divisor == 0:
                fatores.append(divisor)
                n //= divisor
            divisor += 1
        
        return fatores



def combinacoes(m, n):
    if n > m:
        return 0  
    return math.factorial(m) // (math.factorial(m - n) * math.factorial(n))



def remove_repeticoes(lista):
    return list(set(lista))


def calcula_moda(lista):
    contagem = Counter(lista)  # Conta a frequência de cada elemento
    max_frequencia = max(contagem.values())  # Encontra a frequência máxima
    modas = [item for item, frequencia in contagem.items() if frequencia == max_frequencia]  # Retorna os elementos com a frequência máxima
    return modas


def uniao_conjuntos(lista1, lista2):
    return list(set(lista1) | set(lista2))