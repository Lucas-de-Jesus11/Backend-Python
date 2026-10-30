'''
Métodos Especiais (Dunder Methods) em Python:
Os métodos especiais (também chamados de "dunder methods"
porque têm double underscores __) são métodos pré-definidos em
Python que permitem que você personalize o comportamento
de objetos em situações específicas, como:
    Criação de objetos (__init__)
    Representação em string (__str__, __repr__)
    Operações matemáticas (__add__, __sub__)
    Comparação entre objetos (__eq__, __lt__)
    Tamanho de objetos (__len__)
    Acesso a elementos (__getitem__, __setitem__)
Eles são fundamentais para implementar comportamentos
intuitivos em classes personalizadas.
'''

'''
Método construtor __init__ mais comum, chama automaticamente
um objeto usando para inicializar atributos
'''
'''class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#chamada do método
pessoa = Pessoa("Fulano", 20)
print(pessoa.nome, pessoa.idade)'''

'''
Método especial para string  __str__ e __repr__
__str__ retorna uma string mais legivel do objeto (para usuário)
__repr__ retorna uma string mais técnica do objeto (para dev)
'''

'''class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    #método especial para retornar uma string do objeto
    def __str__(self):
        return f"Livro: {self.titulo} Autor: {self.autor}"
    
    #método epecial para retornar uma string do objeto mais técnica
    def __repr__(self):
        return f"Livro: '{self.titulo}' Autor: '{self.autor}'"
livro = Livro("O Hobbit", "J.R.R Tolkien")
#método de str e repr
print(str(livro))
print(repr(livro))'''

'''
Método __len__ tamanho do objeto = a função len()
'''
'''class Playlist:
    def __init__(self, musicas):
        self.musicas = musicas
    
    def __len__(self):
        return len(self.musicas)

#chamada do objeto
playlist = Playlist(["musica1","musica2","musica3","musica4"])
#quantidade de música na playlist
print(len(playlist))#4'''

'''
Métodos especiais para operações matemáticas
__add__= soma, __sub__=subtração, __mul__=multiplicação, __truediv__=divisão
(+,-,*,/)
'''
'''class Operacao:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, num):
        return Operacao(self.x + num.x, self.y+num.y)
    def __str__(self):
        return f"Operação({self.x}, {self.y})"

#criar os números
p1 = Operacao(1, 2)
p2 = Operacao(3, 4)
soma = p1 + p2
print(soma)'''
'''
chamada do p1__add__(p2) saída: Operação(4, 6)
'''


#Comparação de objetos: __eq__ __lt__ comparação como ==, <>
'''class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __eq__(self, numero):
        return self.nota == numero.nota
    
    def __lt__(self, numero):
        return self.nota < numero.nota
#criar dois alunos e comparar as notas
aluno1 = Aluno("fulano", 8.5)
aluno2 = Aluno("ciclano", 7.0)
print(aluno1==aluno2) #false
print(aluno1 < aluno2) #false'''

'''
Método para acessar elementos do objeto
__getitem__ e __setitem__ permite acessar com o get e modificar
com set usando o objeto[chave]=parecido com dicionário
'''
'''class ListaPersonalizada:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def __getitem__(self, indice):
        return self.elementos[indice]#acessa o item
    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor#modifica o elemento
#criar uma lista
lista =ListaPersonalizada([10, 20, 30, 40, 50])
#acessar
print(lista[0]) #saida 10
#modificar
lista[1] = 99#20 vira 99
print(lista[1])#99'''


#__call__ torna um objeto chamácel permitindo que o objeto seja chamado como uma função 
'''class Multiplicar:
    def __init__(self, numero):
        self.numero = numero
    def __call__(self, x):
        return x * self.numero
#chamar o objeto
dobro = Multiplicar(2)
print(dobro(5))#10'''

'''
Quando usar métodos especias?
Quando você quer que o objeto se comporte como uma lista ou dicionário
dicionário __getitem__ __setitem__

Para definir representação string como __str__
para definir operadores(+,-) __add__
para definir comparação ==,<,> __eq__ 
'''

#Exercicio para treinamento de POO
'''
Projeto cadastrar aluuno: sistema para calcular 3 notas de 0 a 10
fazer a média das notas, verificar a média do aluno, 
maior ou igual a 6 aprovado, menor que 6 reprovado
salvar e armazenar em uma lista
'''
