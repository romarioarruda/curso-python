#!/usr/bin/python3

alunos = [
    { "nome": "Romário Arruda", "nota": 10 },
    { "nome": "Tati Lima", "nota": 8 },
    { "nome": "Maria Julia", "nota": 6 },
    { "nome": "Alan Jorge", "nota": 5 }
]

aprovados = lambda aluno: aluno['nota'] >= 7
reprovados = lambda aluno: aluno['nota'] < 7

lista_aprovados = list(filter(aprovados, alunos))
lista_reprovados = list(filter(reprovados, alunos))

print('Alunos aprovados:')
print(lista_aprovados)

print('\n')

print('Alunos reprovados:')
print(lista_reprovados)