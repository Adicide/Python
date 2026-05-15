# 20. Escreva um programa que calcula e exibe a soma: 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, onde n é fornecido pelo usuário.

n = int(input('Digite um número: '))

soma = 0
for denominador in range(1, n+1):
    divisão = 1 / denominador
    soma += divisão
print(f'\nSoma parcial da série harmônica: {soma}')