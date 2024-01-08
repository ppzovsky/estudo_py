# for i in range(10):
#     print (i)

# for i in range(1, 11):
#     print (i)

# for i in range(1, 110, 9):
#     print (i)

# o primeiro numero e o inicio, o seguindo o fim e o terceiro o passo

# for i in range(30, 2, -3):
#     print (i)

nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=',')

texto = 'coisa linda'
print('\n')

for l in texto:
    print(l, end='#')

dados = {
    'nome': 'pp',
    'idade': 23,
    'status': 'apaixonado'
}

print('\n')
for k, v in dados.items():
    print(k, '--->',  v)

print('')
for v in dados.values():
    print(v, end=' ')

print('\n')
for k in dados.keys():
    print(k, end=' ')
