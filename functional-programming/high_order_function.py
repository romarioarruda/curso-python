#!/usr/bin/python3


def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

def processar(titulo, lista, funcao):
    if not callable(funcao):
        raise Exception(f'Parâmetro "{funcao}" não é um callable.')
    
    print(f'Processando: {titulo}')
    
    for i in lista:
        print(i, '=>', funcao(i))



if __name__ == '__main__':
    processar('Dobro de 1 a 10', range(1, 11), dobro)
    processar('Qadrado de 1 a 10', range(1, 11), quadrado)