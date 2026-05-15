# 16. Escreva um programa que lê números reais do usuário enquanto o usuário não digitar um número negativo, 
# e ao final exibe a soma de todos os valores lidos (sem incluir o negativo).

soma = 0
for i in range(999999999999999999999999999999999999999999999):
    num = float(input('Digite um número: '))
    if num < 0:
        break
    
    soma += num
print(f'\nSoma: {soma}')