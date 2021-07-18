# Vamos aprimorar o código:  cadastro de jogador de futebol.py 
# que foi desenvolvido no Code Lab da aula 14. Faça conm que o seu código 
# funcione para vários jogadores, incluindo um sistema de visualização de 
# detalhes de aproveitamento de cada jogador.
class Jogador():
    def __init__(self,nome, partidas):
        self.nome = nome
        self.partidas = partidas
    def calculo(self,dic):
        gols = []
        for i in range(self.partidas):
            gol = int(input('Quantos jogos fez nessa partida?\n'))
            gols.append(gol)
            dic[self.nome] = [(sum(gols) // games), sum(gols)]
        return print(f'O jogador {self.nome}, fez uma media de {dic[self.nome][0]}, gols por partida, com um total de {dic[self.nome][1]} gols')
jogo = {}
condition =''
while condition != 'NAO':
    name = input('Qual nome do jogador?\n')
    games = int(input('Quantas partidas Jogou?\n'))
    jogador = Jogador(name, games)
    jogador.calculo(jogo)
    condition = input('Deseja adicionar outro jogador?\n').upper().replace('Ã','A').strip()