'''
Sisema de Gerenciamento de livro
'''
class Livro:
    def __init__(self, titulo, autor, ano):
        #definir os atributos
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    #metodo
    def detalhe(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de publicação: {self.ano}")

class Biblioteca:
    def __init__(self):
        self.livros = [] #lista vazia

    #metodo para add livro a lista
    def add_livro(self, livro):
        self.livros.append(livro) #add a lista
    
    #def para exibir 
    def lista_livros(self):
        print("Livros na biblioteca")
        #for para exibir na vertical
        for i in self.livros: #for na lista
            i.detalhe()

#criar dois livros
livro1 = Livro("O senhor dos anéis", "J.R.R Tolkien", 1954)
livro2 = Livro("O Hobbit", "J.R.R Tolkien", 1937)

#adicionar os livros
biblioteca = Biblioteca()
biblioteca.add_livro(livro1)
biblioteca.add_livro(livro2)

#Exibir os livros
biblioteca.lista_livros()