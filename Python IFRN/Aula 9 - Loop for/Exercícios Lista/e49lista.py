# 49. Escreva um programa que lê n valores inteiros e exibe, ao final:

# a soma total,
# a média,
# o maior valor,
# o menor valor,
# a quantidade de valores acima da média.

n = int(input('Digite quantos números serão lidos: '))
print('')

soma = 0
listanums = []
for _ in range(n):
    num = int(input('Insira um número: ')) 
    soma += num
    listanums.append(num)

media = soma / n

acima_media = 0
for a in listanums:
    if a > media:
        acima_media += 1

maior = max(listanums)
menor = min(listanums)

print(f'\nSoma total: {soma}')
print(f'Média: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Quantidade de valores acima da média: {acima_media}')