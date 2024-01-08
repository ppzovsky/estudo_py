x = 0

# while x != 1:
#     x = float(input('Informe o numero ou 1 para sair: '))

# print ('FIM')

nota = 0
total = 0
qtd = 0
while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        total += nota
        qtd += 1

print('\n')
print(f'o total das notas e {total}')
print(f'a media das notas e {total/qtd}')
print(f'a turma tem {qtd} alunos')
