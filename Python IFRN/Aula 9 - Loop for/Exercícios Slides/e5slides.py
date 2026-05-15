palavra = input('Digite uma palavra: ')
vogais = 0

print('')
for letra in palavra:
    if letra in 'AEIOUaeiou':
        vogais += 1
print(f'Total de vogais: {vogais}')