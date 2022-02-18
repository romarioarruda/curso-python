#!/usr/bin/python3

def fatorial(n):
    return n * (fatorial(n - 1) if (n - 1) > 1 else 1)


print(fatorial(5))