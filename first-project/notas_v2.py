#!/usr/bin/python3

notas = [
    { "nome": "Romário Arruda", "nota": 10 },
    { "nome": "Tati Lima", "nota": 8 },
    { "nome": "Maria Julia", "nota": 6 },
]

aprovados = []
reprovados = []

for nota in notas:
    if nota['nota'] >= 7:
        aprovados.append(nota)
    elif nota['nota'] < 7:
        reprovados.append(nota)


print(aprovados)
print(reprovados)