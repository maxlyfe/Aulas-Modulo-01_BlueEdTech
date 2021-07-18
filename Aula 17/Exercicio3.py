# Desafio 3 - Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm
class Pessoa():
    def __init__(self, nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self,comando=1):
        self.idade += comando
        if self.idade < 21:
            self.altura +=0.5
    def comer(self):
        self.peso += 3
    def emagrecer(self):
        self.peso -+ 2
    def resultado(self):
        return print(f'{self.nome}\n{self.idade}\n{self.peso}\n{self.altura}')
          
nomeUsuario = input('Qual é o nome do Avatar?\n').upper()
idadeUsuario = int(input('Qual é a idade do Avatar?\n'))
pesoUsuario = float(input('Qual é o peso do Avatar?\n').replace(',','.'))
alturaUsuario = float(input('Qual é a altura do Avatar?\n').replace(',','.'))
usuario = Pessoa(nomeUsuario,idadeUsuario,pesoUsuario,alturaUsuario)
escolha = int(input('O que deseja fazer?\n[1] ENVELHECER \n[2] ENGORDAR\n[3] EMAGRECER\n[4] SAIR\nSUA ESCOLHA = '))
if escolha == 1:
    envelhecendo = int(input('Quantos anos você deseja que se passem?\n'))
    usuario.envelhecer(envelhecendo)
elif escolha == 2:
    usuario.emagrecer()
print(f'As caracteristicas do seu Avatar são:\n{usuario.resultado()}')