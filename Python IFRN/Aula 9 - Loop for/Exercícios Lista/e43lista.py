# 43. Escreva um programa que lê números inteiros positivos do usuário enquanto o usuário não digitar um valor negativo, 
# e ao final exibe quantos dos números lidos são pares e quantos são ímpares.

pares = 0
impares = 0
for i in range(2**1000):
    num = int(input('Digite um número: '))
    if num < 0:
        break
    else:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'\nQuantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')
