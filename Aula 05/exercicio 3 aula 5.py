#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o 
# usuário quer ou não continuar. No final, mostre:

#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.


cadastro_idade = print(int(input('Qual é a sua idade?\n')))
cadastro_homem = print(input('Você é homem?\nSim ou Não\n'))
cadastro_mulher = input('Você é mulher?\nSim ou Não\n')

idade = cadastro_idade
homem = cadastro_homem.replace(' ', '').capitalize().replace('a','ã')
mulher = cadastro_mulher.replace(' ', '').capitalize()

quant_homem = 0
quant_mulher = 0
maiores_18 = 0

if homem == 'Não':
    print(mulher)


continuar = input('Deseja continuar?\nSim ou Não\n')
con_res = continuar.replace(' ', '').capitalize().replace('a','ã')


while cadastro_idade == True and cadastro_homem == True and cadastro_mulher == True:
    input(con_res)
while con_res == 'Sim':
    
    


