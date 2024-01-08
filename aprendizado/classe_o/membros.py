class Contador:
    contador = 0  # atributo de classe, pois para atributo de instancia tem que ser criado atraves do __init__

    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    @staticmethod
    def maisum(n):
        return n+1

# a partir de uma instancia eu possso acessar uma classe
# com isso posso acessar um class method direto de uma classe


print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.maisum(99))

# oss atributos d einstancia sao unicos para cada instancia, enquanto os atributos de classe vao ser compartilhados por toda classe
