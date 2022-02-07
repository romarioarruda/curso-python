#!/usr/bin/python3

def uppercase_decorator(function):
    def decorator(*args, **kwargs):
        return function(*args, **kwargs).upper()
    
    return decorator


def lowercase_decorator(function):
    def decorator(*args, **kwargs):
        return function(*args, **kwargs).lower()
    
    return decorator


@uppercase_decorator
def nome(nome):
    return nome

@lowercase_decorator
def sobrenome(sobrenome):
    return sobrenome

if __name__ == '__main__':
    print(nome('romario'))
    print(sobrenome('ARRUDA'))