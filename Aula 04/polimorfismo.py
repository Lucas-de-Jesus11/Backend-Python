'''
Polimosfismo:Diferentes classes podem ter métodos com o mesmo
nome, mas com comportamento diferente.
parecido com herança
polimorfismo com formas de circulo e retangulo
'''
class Forma: #class pai
    #método da classe
    def area(self): #area de uma forma geométrica
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

#chamar a class pai
forma = Forma()#cria a instância
#inputs de largura e altura
largura = int(input("Entre com a largura: "))
altura = int(input("Entre com a altura: "))
#chamar a classe filho do polimorfismo
retangulo = Retangulo(largura, altura)
print(f"Área do retangulo é: {retangulo.area()}")

'''
exercicio polimorfismo para achar a área de um circulo
PI=3.14
'''
raio = int(input("Digite o raio do circulo: "))
circulo = Circulo(raio)
#print
print(f"Área do círculo é: {circulo.area()} ")