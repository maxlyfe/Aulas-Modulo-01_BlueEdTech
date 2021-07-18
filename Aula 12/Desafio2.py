# 4.	 Desafio: Continuando o exercício 3 crie agora um boletim escolar, 
# seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, 
# o programa tem que calcular a média desse aluno e mostrar a situação dele, seguindo 
# os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, as 
# 5 notas, as médias e as situações dos 15 alunos de uma vez só.
alunos = {}
for i in range(3):
    nome=input('Qual é o seu nome?\n')
    lista_notas=[]
    soma=0
    for u in range(5):
        nota=float(input('Digite a sua nota:\n'))
        lista_notas.append(nota)
        soma=sum(lista_notas)
        media=soma/5
    situacao= 0
    if media > 5 and media <= 6.9:
        situacao='Recuparação'
    elif media >= 7:
        situacao='Aprovado'
    else:
        situacao='Reprovado'
    alunos[nome]= lista_notas, media,situacao
print(alunos)