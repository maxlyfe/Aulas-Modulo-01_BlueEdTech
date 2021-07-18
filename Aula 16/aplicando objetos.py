# 1.a) Crie uma classe pessoa com os seguintes atributos: nome,
# sobrenome e idade.
# # 1.b) Acrescente a classe criada um método para mostrar os dados de
# uma pessoa.
# # 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e
# métodos.
class Pessoa():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade=idade
    def dados(self):
        print(f'O nome é {self.nome}')
        print(f'O sobrenome é {self.sobrenome}')
        print(f'A idade é {self.idade}')

humano = Pessoa('Max','LyFe',28)

humano.dados()
print(type(humano))
print(vars(humano))
print(type(vars(humano)))
print(humano.nome,humano.sobrenome,humano.idade)