# 34. Escreva um programa que recebe dois inteiros positivos a e b e calcula o Máximo Divisor Comum (MDC) usando o algoritmo de Euclides com for.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
a_original = a
b_original = b

for _ in range(max(a, b)):
    if b == 0:
        break
    r = a % b
    a = b
    b = r
print(f'\nMDC({a_original}, {b_original}) = {a}')