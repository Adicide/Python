# 44. Escreva um programa que imprime uma escada de n degraus usando o caractere *. Cada degrau i tem i asteriscos.

n = int(input('Digite a quantidade de degraus: '))

for degrau in range(1, n+1):
    print('*' * degrau)