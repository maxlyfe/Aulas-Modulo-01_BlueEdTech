class Pessoa:
    def __init__(self,nome, idade, cpf, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
    def nome(self):
        self.nome = self.nome
        return self.nome
class Advogado(Pessoa):
    def __init__(self,nome,idade,cpf,telefone,oab):
        super().__init__(nome,idade,cpf,telefone)
        self.oab=oab

class Medico(Pessoa):
    def __init__(self,nome,idade,cpf,telefone,crm):
        super().__init__(nome,idade,cpf,telefone)
        self.crm=crm

#pessoa = Pessoa('Max',28,'011.909.259-07','(22)98103-8642') #construtor
advogado = Advogado('Max',28,'011.909.259-07','(22)98103-8642','Oab 14513584') #construtor
medico = Medico('Max',28,'011.909.259-07','(22)98103-8642','Crm 213') #construtor

#print(medico)
nome = (Pessoa.nome)
print(nome)