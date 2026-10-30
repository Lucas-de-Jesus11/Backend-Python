#aula 04 POO em python

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

#básica de poo em python
class Pessoa:
    def __init__(self, nome): #atributo
        self.nome = nome
    def apresentar(self): #método
        print(f"Olá {self.nome}")
#consumir o objeto usando uma variável
nome = "Lucas"
#input("Digite o nome: ")
pessoa = Pessoa(nome)
#chamar o método
pessoa.apresentar()

'''
POO: usando um sistema simples de classificar destino
como viagem
'''

#class viagem
class Viagem:
    def __init__(self, destino):
        self.destino = destino
#consumir o objeto para criar os destinos
viagem_0 = Viagem("Paris")
viagem_1 = Viagem("Havaí")
viagem_2 = Viagem("Japão")
viagem_3 = Viagem("Tailândia")
viagem_4 = Viagem("Londres")
#lista os destinos em uma lista
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4]
#pegar o nome do viajante e o destino escolhido
viajante = input("Digite o seu nome: ")
print(f"{viajante}: temos 5 destinos disponiveis")
print("""
0- Paris
1- Havaí
2- Japão
3- Tailândia
4- Londres
""")
selecionado = int(input("Selecione o destino: "))
#acessar o destino pelo indice da lista
#criar uma variavel para armazenar o destino
#destino_selecionado = lista_viagem[selecionado].destino
print(f"{viajante}, seu destino {lista_viagem[selecionado].destino} está confirmado")