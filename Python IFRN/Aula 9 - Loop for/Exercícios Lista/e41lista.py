# 41. Escreva um programa que lê n pares de números inteiros (a, b) 
# e, para cada par, informa qual é o maior, qual é o menor, ou se são iguais.

n = int(input('Digite quantos pares vão ser lidos: '))
print('')

for i in range(n):
    a = int(input('Insira um número: '))
    b = int(input('Insira outro número: '))
    
    maior = max(a, b)
    menor = min(a, b)
    
    if a == b:
        print(f'Os dois números são iguais.\n')
    else:
        print(f'\nMaior: {maior}')
        print(f'Menor: {menor}\n')