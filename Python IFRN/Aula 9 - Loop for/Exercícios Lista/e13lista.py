# 13. Escreva um programa que recebe um número inteiro positivo n e imprime os múltiplos de 3 entre 1 e n.

n = int(input('Digite um número: '))
print('')

for i in range(1, n+1):
    if i % 3 == 0:
        print(i)