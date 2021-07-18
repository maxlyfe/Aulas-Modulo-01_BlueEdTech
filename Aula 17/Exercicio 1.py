#Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, 
# crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. 
# Não esqueça que os lançamentos são feitos de forma randômica.
import random
class lancador():
    def __init__(self,lados):
        self.lados=lados
    def lancar(self):
        self.lados = self.lados
        if self.lados == 'Moedas':
            self.lados = 2
            sorteio = random.randint(1,2)
            if sorteio == 1:
                return 'Cara'
            elif sorteio == 2:
                return 'Coroa'
        if self.lados == 'Dado':
            sorte = random.randint(1,6)
            return sorte

usuario = input('Você que jogar com uma moeda ou um dado?\n')
resposta = lancador(usuario)
print(resposta.lancar())
