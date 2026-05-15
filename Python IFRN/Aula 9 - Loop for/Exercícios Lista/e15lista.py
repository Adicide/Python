# 15. Escreva um programa que lê números inteiros do usuário enquanto o usuário não digitar 0, e ao final exibe a quantidade de números lidos (sem contar o zero).

qntd_nums = 0
for i in range(999999999999999999999999999999999): # Número grande pq só pode usar for, e não existe um equivalente do 'while True' no for.
    n = int(input('Digite um número: '))
    
    if n == 0:
        break
    qntd_nums += 1
print(f'\nQuantidade de números: {qntd_nums}')