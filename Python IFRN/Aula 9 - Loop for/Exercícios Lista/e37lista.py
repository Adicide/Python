# 37. Escreva um programa que recebe um inteiro positivo n e exibe o número de dígitos de n.

n = int(input('Digite um número: '))
n_str = str(n)

digitos_n = 0
for i in range(len(n_str)):
    digitos_n += 1
print(f'\n{n} tem {digitos_n} dígitos.')