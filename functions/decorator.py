#!/usr/bin/python3

def logs(function):
    def decorator(*args, **kwargs):
        print(f'Chamando função: {function.__name__}')
        print(f'Args: {args}')
        print(f'KWargs: {kwargs}')
        
        resultado = function(*args, **kwargs)
        
        print(f'Resultado da chamada: {resultado}')
        
        return resultado
    
    return decorator


@logs
def soma(x, y):
    return x + y

@logs
def subtrair(x, y):
    return x - y

if __name__ == "__main__":
    soma(2, 2)
    subtrair(5, y=3)