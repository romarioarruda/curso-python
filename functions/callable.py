#!/usr/bin/python3

def diga_ola():
    print('Olá mundo')


def chama_funcao(func):
    if callable(func):
        func()


if __name__ == "__main__":
    chama_funcao(diga_ola)
    chama_funcao('12121')
    chama_funcao(12121)