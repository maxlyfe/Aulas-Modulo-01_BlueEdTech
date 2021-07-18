# 2) Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.

class Conta():
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def quantidade(self):
        self.saldo = self.saldo
        return self.saldo
    def sacar(self,valor):
        self.saldo -= valor
        return self.saldo
    def depositar(self,dinheiro):
        self.saldo = dinheiro
        return self.saldo
valorEmConta = 50000
cliente = input('Digite o seu nome:\n')
infoconta=Conta(cliente,valorEmConta)
# print(f'{cliente} O seu saldo atual é de R${infoconta.quantidade}')
acao = input('O que você deseja realizar? Depositar/Sacar:\n').upper()
if acao == 'Depositar':
    print(f'{cliente} O valor em conta agora é de R${infoconta.depositar}')
elif acao == 'Sacar':
    print(f'{cliente} O valor em conta agora é de R${infoconta.sacar}')