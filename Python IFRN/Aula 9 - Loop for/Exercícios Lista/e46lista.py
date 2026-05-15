# 46. Escreva um programa que lê n números reais e classifica cada um como:

# "pequeno" se o valor for menor que 10,
# "médio" se o valor estiver entre 10 e 100 (inclusive),
# "grande" se o valor for maior que 100.

# Ao final, exibe a contagem de cada categoria.

n = int(input('Digite quantos números vão ser lidos: '))
print('')

pequenos = 0
medios = 0
grandes = 0
for i in range(n):
    num = float(input('Insira um número: '))
    if num < 10:
        print(f'{num} é Pequeno.\n')
        pequenos += 1
    elif 10 <= num <= 100:
        print(f'{num} é Médio.\n')
        medios += 1
    elif num > 100:
        print(f'{num} é Grande.\n')
        grandes += 1
print(f'Quantidade de números pequenos: {pequenos}')
print(f'Quantidade de números médios: {medios}')
print(f'Quantidade de números grandes: {grandes}')