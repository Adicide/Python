# 42. Escreva um programa que recebe um inteiro positivo n 
# e exibe todos os números no intervalo [1, n] que são simultaneamente divisíveis por 2 e por 7.

n = int(input('Digite um número: '))
print(f'\nDivisores de 2 e 7 no intervalo [1, {n}]:')

for i in range(1, n+1):
    if i % 2 == 0 and i % 7 == 0:
        print(i)