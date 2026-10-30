'''
Herança:Uma classe pode herdar atributos e métodos de outra
classe(chamada de classe pai ou classe base)
'''
#exemplo de POO herança
#classe pai, classe base, super classe

class Animal: #classe pai
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        print(f"{self.nome} está fazendo um som")

#classe filho que vai herdar a classe pai
class Cachorro(Animal): #subclass
    '''após herdar a classe pai, pode chamar as funções da classe pai'''
    def fazer_som(self):
        print(f"{self.nome} está latindo")
    
#subclass
class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} está miando")

#classe pai genérica
#classe filho define melhor os métodos
#chamando a class pai
animal = Animal("Animal xyz")
animal.fazer_som()

#class filho
cachorro = Cachorro("Rex")
cachorro.fazer_som()

#class filho gato
gato = Gato("Felix")
gato.fazer_som()