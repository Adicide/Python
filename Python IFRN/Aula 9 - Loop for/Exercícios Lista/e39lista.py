# 39. Escreva um programa que simula um menu com as opções:

# 1 - Somar dois números
# 2 - Subtrair dois números
# 3 - Sair

# O programa deve repetir o menu enquanto o usuário não escolher a opção 3.

from time import sleep

for i in range(2**1000):
    print('1 - Somar dois números')
    print('2 - Subtrair dois números')
    print('3 - Sair')
    opção = int(input('Insira uma opção: '))
    if opção == 3:
        print('\nSaindo do programa...')
        sleep(2)
        print('Você saiu do programa.')
        break
    elif opção == 1 or opção == 2:
        print('')
    else:
        print('ERRO: Opção inválida. Tente novamente.\n')