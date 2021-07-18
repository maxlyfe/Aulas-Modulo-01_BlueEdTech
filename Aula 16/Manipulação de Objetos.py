class Mamifero():
    def __init__(self,nome,pelo,cor,tamanho,idade):
        self.nome = nome
        self.pelo = pelo
        self.cor = cor
        self.tamanho = tamanho
        self.idade = idade      

    def crecer(self):
        self.idade +=1
    def locomover(self):
        print(f'O {Mamifero} está andando')
    def comer(self):
        self.tamanho = 'Grande'
cachorro = Mamifero('Doby','medio','marrom','grande',5)
print(type(cachorro))
print(vars(cachorro))
print(type(vars(cachorro)))

cachorro.crecer()
cachorro.locomover()
cachorro.comer()
print(cachorro.nome)