def soma(*nums):
    print(type(nums))
    total = 0
    for n in nums:
        total += n
    return total


def resu(**kwargs):
    print(type(kwargs))
    status = 'aprovado' if kwargs['nota'] >= 6 else 'reprovado'
    return f'{kwargs["nome"]} foi {status}'
