# 30. Escreva um programa que recebe um número inteiro positivo n e verifica se ele é primo.

n = int(input('Digite um número: '))

if n <= 1:
    primo = False
elif n == 2:
    primo = True
else:
    primo = True
        
    for divisor in range(2, n):
        if n % divisor == 0:
            primo = False
            break
        divisor += 1

if primo:
    print(f'\n{n} é Primo.')
else:
    print(f'\n{n} Não é primo.')