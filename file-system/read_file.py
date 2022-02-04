#!/usr/bin/python3
arquivo = open('people.csv')

dados = arquivo.read()

arquivo.close()

for dado in dados.splitlines():
    nome = dado.split(',')[-2]
    idade = dado.split(',')[-1]
    
    print('Nome: {}, Idade: {}'.format(nome, idade))
