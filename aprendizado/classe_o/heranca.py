class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.velocidade

    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade
    

class Uno(Carro):
    pass

class Jetta(Carro):
    def acelerar(self):
        super().acelerar() #o metodo super chama a funcao da classe pai, desta forma acelerar e chamada atraves dele e depois novamente pela propria acelerar 
        return super().acelerar()

c1 = Jetta()

print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.acelerar())