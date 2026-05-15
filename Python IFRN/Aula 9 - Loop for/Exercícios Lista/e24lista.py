# 24. Escreva um programa que recebe um número inteiro positivo n e exibe a soma dos dígitos de n.

n = int(input('Digite um número: '))
n_str = str(n)

soma = 0
for digito in n_str:
    soma += int(digito)
print(f'Soma dos dígitos de {n}: {soma}')