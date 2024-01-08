from functools import reduce

# def adiciona(nota):
#     return nota + 0.5


def adiciona(delta):
    def somar(nota):  # este nome de funcao so vai ser unico dentro do namesspace atual, ou seja, dentro da funcao "adiciona"
        nova_nota = nota + delta
        # funcao min retorna o menor valor entre dois numeros
        return min(nova_nota, 10)
    return somar


notas = [6, 4, 7, 8, 9.2, 4.1, 5.7, 6.7]
notafinal = list(map(adiciona(1), notas))
notafinal2 = list(map(adiciona(0.5), notas))


print(notas)
print(notafinal)
print(notafinal2)

print(min(13, 10))  # teste funcao min


# adicionar um valor a todos os elementos da lista

# for i, nota in enumerate(notas):
#     notas[i] = nota + 0.5

# for i in range(len(notas)):
#     notas[i] = notas[i] + 0.5

# print(notas)

# o reduce e ressponsavel por percorrer os elementos chamando uma funcao para cada
def somar(a, b):
    return a+b


total = reduce(somar, notas, 0)
print(total)
