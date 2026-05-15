# 32. Escreva um programa que recebe um número inteiro n e exibe todos os divisores de n.

n = int(input('Digite um número: '))
print(f'\nDivisores de {n}: ')

for divisor in range(1, n+1):
    if n % divisor == 0:
        print(divisor)