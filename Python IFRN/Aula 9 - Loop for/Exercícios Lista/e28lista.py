# 28. Escreva um programa FizzBuzz: imprima os inteiros de 1 a 30, mas substitua:
# os múltiplos de 3 pela palavra Fizz,
# os múltiplos de 5 pela palavra Buzz,
# os múltiplos de 3 e 5 pela palavra FizzBuzz.

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)