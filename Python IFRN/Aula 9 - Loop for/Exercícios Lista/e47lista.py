# 47. Escreva um programa que simula um jogo de adivinhação: o programa sorteia um número inteiro entre 1 e 100 e o usuário tenta adivinhar. 
# A cada tentativa o programa informa se o chute foi "muito baixo", "muito alto" ou "acertou!". O laço termina quando o usuário acertar.

# Dica: use import random e random.randint(1, 100) para sortear o número.

import random
num = random.randint(1, 100)

for i in range(2**1000):
    tentativa = int(input('Adivinhe qual número estou pensando: '))
    if tentativa < num:
        print('Muito baixo!\n')
    elif tentativa > num:
        print('Muito alto!\n')
    elif tentativa == num:
        print('Você acertou!')
        break