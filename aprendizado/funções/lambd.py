from functools import reduce

alunos = [
    {'nome': 'ana', 'nota': 8},
    {'nome': 'joao', 'nota': 8.5},
    {'nome': 'kobe', 'nota': 6.8},
    {'nome': 'jonas', 'nota': 6},
    {'nome': 'kaue', 'nota': 7.7},
    {'nome': 'fael', 'nota': 9.1}
]
# a funcao filter vai filtrar elementos dentro de uma lista
# lambda e uma funcao anonima, ou sem nome
def aluno_aprovado(aluno): return aluno['nota'] >= 6
def honra(aluno): return aluno['nota'] >= 9
def obter_nota(aluno): return aluno['nota']


def somar(a, b): return a+b


alunos_aprovados = list(filter(aluno_aprovado, alunos))
alunos_honra = list(filter(honra, alunos))
notas_aprovados = list(map(obter_nota, alunos_aprovados))
total = (reduce(somar, notas_aprovados, 0)) / len(alunos)

print(alunos_aprovados)
print(alunos_honra)
print(obter_nota(alunos[3]))
print(notas_aprovados)
print(total)

# mesmo escrevendo com lambda, ap[os fechar e abrir o codigo, ele se alto corrige se transformando em funcoes ]
