#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# print('dias no mes', mdays)

setlocale(LC_ALL, 'pt_BR')

def pega_dias_do_mes(month_name):
    months = {
        'Janeiro': 31,
        'Fevereiro': 28,
        'Março': 31,
        'Abril': 30,
        'Maio': 31,
        'Junho': 30,
        'Julho': 31,
        'Agosto': 31,
        'Setembro': 30,
        'Outubro': 31,
        'Novembro': 30,
        'Dezembro': 31
    }
    
    return months.get(month_name, 0)


if __name__ == "__main__":
    for month in list(month_name):
        if not month: continue
        result = f'{month} - {pega_dias_do_mes(month)} dias'
        print(result)
