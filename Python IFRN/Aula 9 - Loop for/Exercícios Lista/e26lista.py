# 26. Escreva um programa que imprime os números de 1 a 20 e, ao lado de cada número, escreve "par" se o número for par ou "ímpar" se for ímpar.

for i in range(1, 21):
    if i % 2 == 0:
        print(f'{i} é Par')
    else:
        print(f'{i} é Ímpar')