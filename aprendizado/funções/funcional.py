def soma(a, b):
    return a+b


def sub(a, b):
    return a-b


somar = soma
print(somar(3, 4))


def op_bn(fn, op1, op2):
    return fn(op1, op2)


result = op_bn(soma, 13, 48)  # essta resolvendo uma fun;'ao dentro da outra
print(result)

result = op_bn(sub, 13, 48)  # essta resolvendo uma fun;'ao dentro da outra
print(result)

def soma_parcial(a): #um funcao dentor da outra, para tornar a execucao final tardia
    def concluir(b):
        return a+b 
    return concluir

#serve para melhorar o tempo de processamento como em problemas de linguegem funcional
fn = soma_parcial(10)
rf = fn(12)
print (rf)