#!/usr/bin/python3

# with garante o fechamento do arquivo.
with open('people.csv') as arquivo:
    with open('people.txt', 'a') as saida:
        for dado in arquivo:
            nome = dado.strip().split(',')[-2]
            idade = dado.strip().split(',')[-1]
            
            print('Nome: {}, Idade: {}'.format(nome, idade), file=saida)

if arquivo.closed:
    print('Arquivo CSV fechado com sucesso!')

if saida.closed:
    print('Arquivo TXT fechado com sucesso!')