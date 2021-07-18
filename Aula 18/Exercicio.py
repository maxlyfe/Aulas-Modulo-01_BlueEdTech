#Crie uma classe chamada bombaCombustivel, com no minimo esses atributos:
# i tipoCombustivel.
# ii valorLitro.

class BombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro=0,quantidadeCombustivel=0):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    @property
    def preco(self,preco=0):
        preco = self.valorLitro
        return preco
    @property
    def litros(self,litros):
        litros = self.quantidadeCombustivel
        return litros
    def abastecerPorValor(self, valor):
        valor = valor / self.valorLitro
        return valor
    def abastecerPorLitro(self, litros=0):
        litros = litros * self.valorLitro
        return litros

aditivada = BombaCombustivel('Aditivada',6.78,5000)
comum = BombaCombustivel('Gasolina Comum',6.58,14000)

escolhaCombustivel = print('Que tipo de combustivel você deseja abastecer?\n[1] Comum\n[2] Aditivada:\n')
