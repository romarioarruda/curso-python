#!/usr/bin/python3
from functools import reduce

alunos = [
    { "nome": "Romário Arruda", "nota": 10 },
    { "nome": "Tati Lima", "nota": 8 },
    { "nome": "Maria Julia", "nota": 6 },
    { "nome": "Alan Jorge", "nota": 5 }
]

lambda_soma = lambda notas, aluno: notas + aluno['nota']
soma_notas = reduce(lambda_soma, alunos, 0)


print(f'Soma das notas: {soma_notas}')