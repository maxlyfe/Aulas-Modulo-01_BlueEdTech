##exemplo simples do for

# usuario = input('Digite um texto:\n')
# for i in usuario:
#     print(i)



## for em lista

lista = [10,20,30,40,50]
print(len(lista))
print(lista)
print(type(lista))
### range cria uma secuencia de numeros do tamanho a minha lista de 0 a ...
### for i in range(0,len(lista),2): pega a partir do indice 0 até o final da lista pulando de 2 em 2.
#print(i+1,lista) faz printar o indice iniciando com o numero inicial a partir de 1.
for i in range(len(lista)):  # -> percorre o tamanho da lista.
    print(i) #-> printa o indice
    print(i, lista[i]) #-> printo o indece + a lista
      

for i in lista:  # -> percorre os itens da lista.
    print(i) #-> printa a lisata

  