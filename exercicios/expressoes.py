def mdc(a,b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    
    return a

def mmc(a,b):

    if a > b:
        maior = a
    else:
        maior = b

    for i in range(maior):
        aux = a * i
        if (aux % b) == 0:
            mmc = aux

    print(mmc)
