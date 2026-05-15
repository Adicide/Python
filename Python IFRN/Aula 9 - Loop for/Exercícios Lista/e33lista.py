# 33. Escreva um programa que lê números inteiros enquanto o usuário não digitar 0, e ao final exibe a soma dos números pares e a soma dos números ímpares lidos.

soma_pares = 0
soma_impares = 0
limite = 2 ** 1000
for i in range(limite):
    num = int(input('Digite um número: '))
    
    if num == 0:
        break
    else: 
        if num % 2 == 0:
            soma_pares += num
        else:
            soma_impares += num
print(f'\nSoma dos pares: {soma_pares}')
print(f'Soma dos ímpares: {soma_impares}')