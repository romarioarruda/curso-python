#!/usr/bin/python3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def fibonacci(numeros=None, limite=100):
    numeros = numeros or [0, 1]
    if numeros[-1] < limite:
        numeros.append(sum(numeros[-2:]))

        return fibonacci(numeros, limite)
    
    return numeros


if __name__ == "__main__":
    print(fibonacci([0, 1], 1000))
    print(fibonacci())