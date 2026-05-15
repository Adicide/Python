# 40. Escreva um programa que recebe um inteiro positivo n e determina se n é um número perfeito 
# (um número é perfeito se a soma de seus divisores próprios é igual a ele mesmo, ex: 6 = 1+2+3).

n = int(input('Digite um número: '))

soma = 0
for divisor in range(1, n):
    if n % divisor == 0:
        soma += divisor

if soma == n:
    print(f'\n{n} é um número Perfeito.')
else:
    print(f'\n{n} Não é um número perfeito.')