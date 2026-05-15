# 14. Escreva um programa que recebe um número inteiro base e um número inteiro positivo expoente, 
# e calcula base ** expoente sem usar o operador ** — use apenas multiplicações repetidas com for.

base = int(input('Insira a base: '))
expoente = int(input('Insira o expoente: '))

potencia = 1
for i in range(expoente):
    potencia *= base
print(f'\n{base}^{expoente} = {potencia}')