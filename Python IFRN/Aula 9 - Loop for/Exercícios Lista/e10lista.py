# 10. Escreva um programa que lê 10 números reais digitados pelo usuário e imprime a média aritmética.

soma = 0
for i in range(1, 11):
    n = float(input('Digite um número: '))
    soma += n
média = soma / 10
print(f'\nMédia: {média}')