# 11. Escreva um programa que recebe um número inteiro positivo n e imprime a tabuada de multiplicação de n (de 1 a 10).

n = int(input('Digite um número: '))
n_original = n
print(f'\nTabuada do {n}:')

multiplicação = 0
for i in range (1, 11):
    multiplicação = n * i
    print(f'{n_original} * {i} = {multiplicação}')