from functools import reduce

alunos = [
    {'nome': 'ana', 'nota': 8},
    {'nome': 'joao', 'nota': 8.5},
    {'nome': 'kobe', 'nota': 6.8},
    {'nome': 'jonas', 'nota': 6},
    {'nome': 'kaue', 'nota': 7.7},
    {'nome': 'fael', 'nota': 9.1}
]


def honra(aluno): return aluno['nota'] >= 9
def obter_nota(aluno): return aluno['nota']


def somar(a, b): return a+b


alunos_aprovados = [aluno['nota'] for aluno in alunos if aluno['nota'] >= 8]

print(alunos_aprovados)
