#!/usr/bin/python3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def fibonacci(limite=100):
    numeros = [0, 1]

    while numeros[-1] < limite:
        # numeros.append(numeros[-2] + numeros[-1])
        numeros.append(sum(numeros[-2:]))

    
    return numeros

if __name__ == "__main__":
    resultado = fibonacci(10)
    
    print(resultado)