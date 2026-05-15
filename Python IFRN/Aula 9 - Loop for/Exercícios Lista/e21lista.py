# 21. Escreva um programa que lê n notas de alunos (onde n é fornecido pelo usuário) e exibe a maior nota lida.

n = int(input('Digite a quantidade de notas: '))

listanums = []
for i in range(n):
    nota = int(input('Digite uma nota: '))
    listanums.append(nota)
    
maior_nota = max(listanums)
print(f'\nMaior nota: {maior_nota}')