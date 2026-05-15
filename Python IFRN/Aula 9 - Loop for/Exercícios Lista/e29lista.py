# 29. Escreva um programa que lê n números reais e exibe separadamente a soma dos valores positivos e a soma dos valores negativos.

n = int(input('Digite quantos números serão lidos: '))
print('')

soma_positivos = 0
soma_negativos = 0
for i in range(n):
    num = float(input('Insira um número: '))
    if num > 0:
        soma_positivos += num
    elif num < 0:
        soma_negativos += num
print(f'\nSoma dos valores positivos: {soma_positivos}')
print(f'Soma dos valores negativos: {soma_negativos}')