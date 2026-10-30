'''
POO = Class
PascalCase= 1° letra maiuscula
snake_case= utiliza o underline (_) para_separar_palavras_entre_elas
cARMELcASE= 1° letra minuscula

Componentes principais da POO em Python:
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
#básico do def
def nome_funcao():
    #cria funcionalidade do sistema
    pass

#básico POO em python
class NomeClass: #uma instância
    #método construtor, iniciar os atributos, definir metodo e atributo com função
    def __init__(self, atributo1, atributo2): #__init__ = iniciar a instancia da class
        #1º atributo sempre será o self
        #definir os atributos
        #self.qualquernome1 = atributo1
        #self.qualquernome2= atributo2
        self.atributo1 = atributo1
        self.atributo2 = atributo2
    #função para a ação dos atributos
    def metodo(self): #ação vai ser um print
        print(f"Atributo 1: {self.atributo1}")
        print(f"Atributo 2: {self.atributo2}")
    #ação dos atributos

#criar uma variavel para chamar a class
objeto = NomeClass("Carro Azul", "Carro Rosa")
#chamar a instancia do objeto
objeto.metodo()

#class pessoa, nome e idade
class Pessoa:
    #atributo da pessoa
    def __init__(self, nome, idade):
        #definir os atributos
        self.nome = nome
        self.idade = idade
    #ação do objeto
    def apresentar(self):
        print(f"Meu nome é: {self.nome}")
        print(f"Minha idade é: {self.idade} anos")
#criar uma variavel para chamar o objeto
pessoa = Pessoa("lucas", 20)
#nome = input("Digite seu nome: ")
#idade = input("Digite sua idade: ")
#pessoa = Pessoa(nome, idade)
pessoa.apresentar()

'''
objeto é uma classe, essa classe é uma instancia, que tem
atributos e métodos
Atributos: são características(variaveis) que define o objeto
Método: são funçõs que descreve o comportamento do objeto'
'''