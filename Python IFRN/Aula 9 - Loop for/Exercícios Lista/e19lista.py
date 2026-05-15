# 19. Escreva um programa que imprime os primeiros n termos da progressão aritmética 
# com primeiro termo a e razão r, onde n, a e r são fornecidos pelo usuário.

n = int(input('Digite o número do enésimo termo: '))
a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

print(f'\n{n} primeiros termos da PA: ')
for termo in range(n):
    print(a)
    a += r