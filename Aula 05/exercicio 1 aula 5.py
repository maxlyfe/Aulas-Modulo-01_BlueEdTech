#Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite 
# os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

pergunta = input('Digite M se seu sexo biologico é Masculino\nDigite F se seu sexo biologico é Femenino:\n')


while pergunta != 'M' and pergunta != 'F':
    pergunta = input('Digite M se seu sexo biologico é Masculino\nDigite F se seu sexo biologico é Femenino:\n')


