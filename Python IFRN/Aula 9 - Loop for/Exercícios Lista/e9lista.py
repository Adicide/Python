# 9. Escreva um programa que lê 5 números inteiros digitados pelo usuário e imprime a soma deles.

soma = 0
for i in range(1, 6):
    n = int(input('Digite um número: '))
    soma += n
print(f'\nSoma: {soma}')