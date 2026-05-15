# 31. Escreva um programa que lê 10 notas (de 0 a 10) e exibe:
# a média das notas,
# a quantidade de alunos aprovados (média ≥ 7),
# a quantidade de alunos reprovados (média < 5),
# a quantidade de alunos em recuperação (5 ≤ média < 7).

# ANOTAÇÕES PESSOAIS:
# Considerar que nota e n = média do aluno

soma = 0
listanums = []
for nota in range(10):
    nota = float(input('Digite uma nota: '))
    listanums.append(nota)
    soma += nota
media = soma / 10

aprovados = 0
reprovados = 0
recuperacao = 0
for n in listanums: # n = nota (usei n para não repetir 'nota')
    if n >= 7:
        aprovados += 1
    elif n < 5:
        reprovados += 1
    elif 5 <= n < 7:
        recuperacao += 1

print(f'\nMédia das notas: {media}')
print(f'Quantidade de alunos aprovados: {aprovados}')
print(f'Quantidade de alunos reprovados: {reprovados}')
print(f'Quantidade de alunos em recuperação: {recuperacao}')