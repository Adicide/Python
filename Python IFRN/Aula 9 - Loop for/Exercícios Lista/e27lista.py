# 27. Escreva um programa que lê 10 números inteiros e exibe quantos são positivos, quantos são negativos e quantos são iguais a zero.

positivos = 0
negativos = 0
zeros = 0
for i in range(10):
    num = int(input('Digite um número: '))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print(f'\nQuantidade de números positivos: {positivos}')
print(f'Quantidade de números negativos: {negativos}')
print(f'Quantidade de números iguais a 0: {zeros}')