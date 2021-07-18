# 2.	Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário 
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , 
# com quantos anos a pessoa vai se aposentar.
#  Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
dicionario = {}
continucao = 0
while continucao != 'Não':
    nome = input('Qual é o seu nome? \n')
    nascimento = int(input('Em que ano você nasceu?:\n'))
    carteira = int(input('Digite os numeros da sua carteira de trabalho:\n'))
    idade = 2021 - nascimento
    dicionario[nome] = nascimento, idade
    if carteira != 0:
        contratacao = int(input('Em que ano você começou a trabalhar?\n'))
        salario = float(input('Qual é o seu salario?\n R$'))
        aposentar = (contratacao + 35) - nascimento
        dicionario[nome] = nascimento, idade, salario, aposentar

    continucao = input('Deseja cadastrar outra pessoa?\n').capitalize().replace(' ','').replace('a','ã')

print(dicionario)
