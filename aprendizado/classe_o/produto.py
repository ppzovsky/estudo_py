class Produto:
    def __init__(self, nome, preco = 3.5, desc=0): #funcao que instancia um novo objeto criando um atributo para este 
        self.nome = nome
        self.__preco = preco
        self.desc = desc

    #metodo é uma função dentro de uma classe 

    @property #faz com que o codigo entenda a funcao a seguir como um atributo da classe ao invés de uma função 
    def precofinal(self): #n necessita nenhum outro parametro pois o self tem acesso a todos
        return (1-self.desc) * self.preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo):
        if novo>0:
            self.__preco = novo
#as classes sao moldes, e os objetos criados a partir destas sao suas instancias 

p1 = Produto('caneta', 3, 0.1) #Produto.__init__(p1)
p2 = Produto('lapis', 1.35, 0.2)

p1.preco =-2
p2.preco = 5.80

print (p1.nome, p2.nome)
print (p1.preco, p2.preco)
print (p1.desc, p2.desc)
print (p1.precofinal, p2.precofinal) 

# para criarmos um atributo privado dentro de uma classe em python usamos __ antes da nomenclatura