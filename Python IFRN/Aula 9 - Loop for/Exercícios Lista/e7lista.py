# 7. Escreva um programa que recebe um número inteiro positivo n e imprime a soma dos números de 1 a n.

n = int(input('Digite um número: '))

soma = 0
for i in range(1, n+1):
    soma += i
print(f'\nSoma dos números de 1 a {n} = {soma}')