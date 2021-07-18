# 3.	DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, 
# e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
lista = []
nome = 0
sexo = 0
idades = []
pessoas = 0
quantidade_F =[]
idade_acima_media = []
media_idade=[]
cadastro=0
while cadastro != 'Não':
    pessoas +=1
    dicionario = {}
    nome=input('Qual é o seu nome?\n').title().strip()
    sexo=input('Qual é o seu sexo? Masculino ou Feminino:\n').capitalize().strip()
    while sexo != 'Masculino' and sexo != 'Feminino':
        sexo=input('Qual é o seu sexo? Masculino ou Feminino:\n').capitalize().strip()
    if sexo == 'Feminino':
        quantidade_F.append(nome)
    idade=int(input('Qual é a sua idade?\n'))
    cadastro = input('Deseja cadastrar outra pessoa?:\n').capitalize().replace('a','ã').replace(' ','')
    dicionario[nome] = sexo, idade
    idades.append(idade)
    lista.append(dicionario)
soma_idade=sum(idades)
media_idade= soma_idade/pessoas
for i in idades:
    if i > media_idade:
        idade_acima_media.append(i)

print()
print(f'Minha lista {lista}')
print()
print(f'As mulheres são {quantidade_F}')
print()
print(f'{idade_acima_media}São as idades que estão acima da media')
print()
print(f'A media de idades é de {media_idade}')