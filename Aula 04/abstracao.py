'''
Abstração: Ocultar a complexidade dos detalhes internos,
expõe apenas o que é necessário para o uso
'''
#exemplo simples da abstração
#abstração precisamos importar um método abstração
from abc import  ABC, abstractmethod #conceito de abstração
class Forma:
    #dizer que é uma classe abstrata
    @abstractmethod #chamar o método abstrato
    def area(self):
        pass    

class Retangulo(Forma):#class filho
    #criar a instância para achar a área do retângulo
    def __init__(self, largura, altura):
       self.largura = largura
       self.altura = altura
    #método para achar a área do retangulo
    def area(self):
         #retornar o resultado da área do retangulo
         return self.largura*self.altura

#subclass filho
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    #método para área do circulo
    def area(self):
        return 3.14*(self.raio)

#não a necessidade de chamar a classe pai
retangulo = Retangulo(10,5)
circulo = Circulo(7) #153,86
print(f"Área do retângulo é: {retangulo.area()}")
print(f"Área do circulo é: {circulo.area()}")