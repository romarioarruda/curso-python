#!/usr/bin/python3
import csv

# with garante o fechamento do arquivo.
with open('people.csv') as arquivo:
    for dado in csv.reader(arquivo):
        print(dado)

if arquivo.closed:
    print('\nArquivo CSV fechado com sucesso!')
