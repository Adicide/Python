# 25. Escreva um programa que recebe um número inteiro positivo n e exibe n na ordem inversa dos dígitos.

n = int(input('Digite um número: '))
n_str = str(n)
digitos_n = len(n_str)

inverso = ''
for digito in range(digitos_n):
    inverso += n_str[digitos_n - 1 - digito]
print(f'Inverso de {n}: {inverso}')