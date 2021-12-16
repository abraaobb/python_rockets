texto = input('Digite uma palavra: ')
vogais = ('a', 'e', 'i', 'o', 'u',)
cont_vogais = 0
for t in texto:
    if t.lower() in vogais:
        cont_vogais += 1
print(cont_vogais)
