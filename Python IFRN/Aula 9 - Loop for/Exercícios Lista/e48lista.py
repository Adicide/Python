# 48. Escreva um programa que recebe um inteiro positivo n e verifica se ele é um palíndromo numérico (lê-se igual de trás para frente).

n = int(input('Digite um número: '))
n_str = str(n)

inverso = ''
for digito in range(len(n_str)):
    inverso += n_str[len(n_str) - 1 - digito]
if int(inverso) == n:
    print(f'{n} é um Palíndromo.')
else:
    print(f'{n} Não é um palíndromo.')