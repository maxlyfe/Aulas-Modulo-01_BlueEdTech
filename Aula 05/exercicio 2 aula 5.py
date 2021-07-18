#Escreva um programa que pede a senha uma senha ao usuário, e 
# só sai do loop quando digitarem
#corretamente a senha. A senha é “Blue123”
#2b - Exiba quantas vezes o usuário errou a digitação.

#senha = 'Blue123'

#usuario = input('Digite a senha:\n')

#while usuario != senha:
#    usuario = input('Digite a senha:\n')
#    if usuario == senha:
#        print('Senha correta.')'


senha = 'Blue123'
usuario = input('Digite a sua senha:\n')
erros = 0
while senha != usuario:
        usuario = input('Senha incorreta!\nDigite novamente: ')
        if usuario==senha:
                print('Acesso liberado!')
        elif erros == 5:
                print('Acesso Bloqueado!')
                break
        erros += 1

print(f'Você errou {erros} vezes')
