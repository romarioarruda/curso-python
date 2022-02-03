#!/usr/bin/python3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def fibonacci(limite=100):
    penultimo = 0
    ultimo = 1
    
    print(f'{penultimo},{ultimo}', end=',')
    
    while ultimo < limite:
        proximo = penultimo + ultimo
        penultimo = ultimo
        ultimo = proximo
        
        print(proximo, end=',')

if __name__ == "__main__":
    fibonacci(1000)