def soma(*args):
    acum = 0
    for a in args:
        acum += a
    return acum


numeros = [1, 2, 3, 4]
print(soma(10, 20, 30, 40))
print(soma(*numeros))
