# 50. Escreva um programa que exibe a seguinte tabela de conversão de temperaturas de 0 °C a 100 °C, 
# e 10 em 10 graus, mostrando Celsius, Fahrenheit e Kelvin. 
# Ao lado de cada linha, classifique a temperatura como "fria" (< 15 °C), "agradável" (15 °C a 25 °C) ou "quente" (> 25 °C).

# Fórmulas: F = C × 9/5 + 32 ; K = C + 273.15

print(f'{"Celsius":<10}{"Fahrenheit":<12}{"Kelvin":<10}{"Classificação"}')
print('-' * 46)

for c in range(0, 101, 10):
    f = c * 9/5 + 32
    k = c + 273.15
    
    if c < 15:
        classificação = 'Fria'
    elif 15 <= c <= 25:
        classificação = 'Agradável'
    else:
        classificação = 'Quente'
        
    print(f'{c:<10}{f:<12.2f}{k:<10.2f}{classificação}')