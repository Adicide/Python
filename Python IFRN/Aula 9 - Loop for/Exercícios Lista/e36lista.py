# 36. Escreva um programa que lê uma senha digitada pelo usuário e continua pedindo a senha enquanto ela estiver incorreta. 
# A senha correta é "python123". Ao acertar, exibe "Acesso permitido".

for i in range(2**1000):
    senha = input('Digite a senha: ')
    if senha == 'python123':
        print('Acesso permitido.')
        break