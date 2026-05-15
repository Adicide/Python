# 45. Escreva um programa que recebe dois inteiros inicio e fim e exibe a soma de todos os números primos no intervalo [inicio, fim].

inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))

soma_primos = 0
for num in range(inicio, fim+1):
    if num <= 1:
        primo = False
    elif num == 2:
        primo = True
    else:
        primo = True

        for divisor in range(2, num):
            if num % divisor == 0:
                primo = False
                break
    
    if primo:
        soma_primos += num
print(f'\nSoma dos números primos no intervalo [{inicio}, {fim}]: {soma_primos}')