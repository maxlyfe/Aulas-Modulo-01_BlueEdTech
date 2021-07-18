# 1.	Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. No final, 
# mostre o conteúdo da estrutura na tela. A média para 
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de 
# recuperação, caso contrário é reprovado.

dicionario = {}
nota = []
nome = input('Qual é o seu nome?\n')

for i in range(3):
    notas = float(input('Qual foi a sua nota?:\n'))
    nota.append(notas)
soma=sum(nota)
media= soma/3
if media > 5 and media <= 6.9:
    print(f'Você esta em recuperação, sua media foi de {media:.2f}')
elif media >= 7:
    print(f'Parabens você foi aprovado!!! sua media foi de {media:.2f}')
else:
    print(f'Você foi reprovado =( sua media foi de {media:.2f}')

dicionario[nome] = nota
print(dicionario)