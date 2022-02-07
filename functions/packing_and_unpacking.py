#!/usr/bin/python3

#  Packing é como se fosse o rest operator do JS
def soma_n_valores(*numeros):
    print(type(numeros))
    total = 0
    
    for num in numeros:
        total += num
        
    return total


if __name__ == "__main__":
    # Unpacking é como o spread operator do JS
    tupla = (1,2,3,4,5)
    print(soma_n_valores(*tupla))