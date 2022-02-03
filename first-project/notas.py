#!/usr/bin/python3
import sys


if not sys.argv[1].isnumeric():
    print("Valor não numérico, parando.")
    sys.exit()


nota = int(sys.argv[1])

if nota > 9:
    print("Passou com honra")
elif nota >= 7:
    print("Passou na média")
elif nota <= 6:
    print("Reprovado")