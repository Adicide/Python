# 8. Escreva um programa que recebe um número inteiro positivo n e imprime o produto (fatorial) de 1 × 2 × ... × n.

n = int(input('Digite um número: '))
n_original = n

fator = n - 1 # O número que vai multiplicar n.
for i in range(n_original-1):
    n *= fator
    fator -= 1
print(f'\n{n_original}! = {n}')