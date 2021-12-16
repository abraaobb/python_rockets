numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# [posicao:quantidade:passos]

print('a lista é: {}'.format(numeros))
# imprimir so os numeros nas posiçoes impares da lista
print('as posiçoes impares: {}'.format(numeros[1::2]))

# imprimir de forma inversa a lista
print('a lista invertida: {}'.format(numeros[::-1]))


outros = [9, 0]

nova = numeros + outros
print(nova)
