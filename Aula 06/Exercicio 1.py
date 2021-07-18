# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte
# quantas vezes aparece as vogais a,e,i,o,u

usuario = input('Digite uma frase:\n')
a=0
e=0
i=0
o=0
u=0
es=0
for item in usuario:
  if item == 'a' or usuario == 'A':
    a+=1
  if item == 'e' or usuario == 'E':
    e+=1
  if item == 'i' or usuario == 'I':
    i+=1
  if item == 'o' or usuario == 'O':
    o+=1
  if item == 'u' or usuario == 'U':
    u+=1
  if item == ' ':
    es+=1
print(f'A frase "{usuario}" tem:\n{es} espaços\n{a} letras a\n{e} letras e\n{i} letras i\n{o} letras o\n{u} letras u') 
