def mdc(a,b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    
    return a

def mmc(a,b):
    return abs(a * b) / mdc(a, b)

def mdc_lista(lista):
    return reduce(mdc, lista)
