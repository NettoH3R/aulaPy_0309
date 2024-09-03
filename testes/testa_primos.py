def testa_primos(n):
    primo = True
    for divisor in range(2,int(n**0.5)+1):
        if n % divisor == 0:
            primo == False
            break
    return primo