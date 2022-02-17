#!/usr/bin/python3

alunos = [
    { "nome": "Romário Arruda", "nota": 10 },
    { "nome": "Tati Lima", "nota": 8 },
    { "nome": "Maria Julia", "nota": 6 },
    { "nome": "Alan Jorge", "nota": 5 }
]

aprovados = lambda aluno: aluno if aluno['nota'] >= 7 else None
reprovados = lambda aluno: aluno if aluno['nota'] < 7 else None

lista_aprovados = list(map(aprovados, alunos))
lista_reprovados = list(map(reprovados, alunos))

if __name__ == '__main__':
    print('Alunos aprovados:')
    print(lista_aprovados)
    print('\n')
    print('Alunos reprovados:')
    print(lista_reprovados)