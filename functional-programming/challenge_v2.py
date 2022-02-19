#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

setlocale(LC_ALL, 'pt_BR')
lista_meses = list(filter(None, list(month_name)))
lista_dias = list(filter(None, mdays))


print(lista_dias)
print(lista_meses)



