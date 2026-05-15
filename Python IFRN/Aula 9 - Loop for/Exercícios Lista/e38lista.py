# 38. Escreva um programa que lê n números inteiros e exibe o maior e o menor valor lido.

n = int(input('Digite quantos números devem ser lidos: '))

listanums = []
for i in range(n):
    num = int(input('Insira um número: '))
    listanums.append(num)
maior = max(listanums)
menor = min(listanums)

print(f'\nMaior número: {maior}')
print(f'Menor número: {menor}')