# 35. Escreva um programa que imprime os primeiros n números da sequência de Fibonacci, onde n é fornecido pelo usuário.

n = int(input('Digite um número: '))
t1 = 0 # 1° termo da sequência de Fibonacci
t2 = 1 # 2° termo da sequência de Fibonacci
soma = 0 

for _ in range(n):
    print(t1)
    soma = t1 + t2
    t1 = t2
    t2 = soma 