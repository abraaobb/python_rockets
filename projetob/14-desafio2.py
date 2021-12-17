# Dada uma palavra criar uma programa para retornar a quantidade de vogais e quantidade de consoantes
print('segundo desafio')
texto = input('Digite uma palavra: ')
vogais = ('a', 'e', 'i', 'o', 'u',)
cont_vogais = 0
cont_consoantes = 0
for t in texto:
    if t.lower() in vogais:
        cont_vogais += 1
    else:
        cont_consoantes += 1
print('quantidade de vogais: {}'.format(cont_vogais))
print('quantidade consoantes: {}'.format(cont_consoantes))