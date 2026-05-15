# 17. Escreva um programa que recebe dois inteiros positivos a e b (com a < b) e imprime todos os inteiros no intervalo [a, b].

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

while a <= 0 or b <= 0:
    print('\nERRO: Cada número deve ser positivo.')
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))

while a >= b:
    print('\nERRO: O primeiro número deve ser menor que o segundo.')
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))  

print('')
for i in range(a, b+1):
    print(i)