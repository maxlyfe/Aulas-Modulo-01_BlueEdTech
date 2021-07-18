#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. 
# No final tudo isso será guardado em um dicionário, incluindo a média de gols por jogo, e o total 
# de gols feitos durante o campeonato.
dicionario={}
gol=[]
nome =input('Qual é o seu nome?\n')
dicionario['Jogador'] = nome
partidas = int(input('Quantos jogos você jogou?\n'))
dicionario['partidas'] = partidas
jogo = 1
for i in range(partidas):
    gols = int(input(f'Quantos gols você fez no jogo {jogo}\n'))
    gol.append(gols)
    jogo +=1
somas=sum(gol)
dicionario['goltotal'] = somas
print(f'O jogador {dicionario["Jogador"]}, jogou {dicionario["partidas"]} partidas\nFez um total de {dicionario["goltotal"]} gols \nE a media de gols é de {somas/partidas:.0f}')
