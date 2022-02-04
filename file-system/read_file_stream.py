#!/usr/bin/python3

try:
    print('Lendo o arquivo CSV.\n')
    arquivo = open('people.csv')

    for dado in arquivo:
        nome = dado.strip().split(',')[-22] # erro aqui
        idade = dado.strip().split(',')[-1]
        
        print('Nome: {}, Idade: {}'.format(nome, idade))
finally:
    print('\nTentando garantir fechamento do arquivo')
    arquivo.close()
    
if arquivo.closed:
    print('\nArquivo fechado com sucesso!')