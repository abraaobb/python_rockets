# Dada uma lista de valores inteiros criar um programa para somar os valores pares e valores ímpares

lista = [1, 8, 6, 4, 9, 4, 3, 0, 6, 12]
soma_par = 0
soma_impar = 0
for l in lista:
    if l % 2 == 0:
        soma_par += l
    else:
        soma_impar += l
print('primeiro desafio')
print('soma dos pares: {}'.format(soma_par))
print('soma dos impares: {}'.format(soma_impar))
