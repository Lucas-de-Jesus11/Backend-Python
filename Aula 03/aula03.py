#Aula03
'''
POO = ClassComponentes principais da POO em Python:
classe: define o molde de um objeto(conjunto de atributos
e métodos) -> PascalCase
objeto:é a instância da classe.
atributos:São as características(variáveis) que os objetos da
classe terão
método:são a funções que descrevem o comportamento dos objetos
Herança:Uma classe pode herdar atributos e métodos de outra
classe(chamada de classe pai ou classe base)
Encapsulamento:É um conceito de ocultar detalhes internos de
de um objeto e proteger os dados de acessos externos
Polimosfismo:Diferentes classes podem ter métodos com o mesmo
nome, mas com comportamento diferente.
Abstração: Ocultar a complexidade dos detalhes internos,
expõe apenas o que é necessário para o uso
'''

#Exemplo criar um objeto carro
class Carro: #objeto instância
    #definir os atributos do carro
    def __init__(self, marca, modelo, ano): #init inicia o objeto
        self.marca = marca #atributo maarca do carro
        self.modelo = modelo #atributo modelo do carro
        self.ano = ano #atributo ano do carro
    
    #metodo do objeto
    def info(self):
        print(f"Carro: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        #fim do objeto

#chamar o objeto
carro1 = Carro("Ford", "Mustang", 1967)
carro2 = Carro("Ford", "Mustang", 1980)
carro3 = Carro("Ford", "Mustang", 2025)
print(carro1, carro2, carro3)
