# 22. Escreva um programa que lê n notas de alunos (onde n é fornecido pelo usuário) e exibe a menor nota lida.

n = int(input('Digite a quantidade de notas: '))

listanums = []
for i in range(n):
    nota = int(input('Digite uma nota: '))
    listanums.append(nota)

menor_nota = min(listanums)
print(f'\nMenor nota: {menor_nota}')