#!/usr/bin/python3

alunos = [
    { "nome": "Romário Arruda", "nota": 10 },
    { "nome": "Tati Lima", "nota": 8 },
    { "nome": "Maria Julia", "nota": 6 },
    { "nome": "Alan Jorge", "nota": 5 }
]

def resultado(aluno):
    aluno['aprovado'] = False

    if aluno['nota'] >= 7:
        aluno['aprovado'] = True
        
        return aluno
    
    return aluno


lista_aprovados = list(map(resultado, alunos))


print('Resultado final:')
print(lista_aprovados)