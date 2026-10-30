class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def detalhe(self):
        print(f"Título: {self.titulo}")

class Biblioteca:
    def __init__(self):
        self.livros = []
    def add_livro(self, livro):
        self.livros.append(livro)
    
    #método para listar os livros
    def listar(self):
        print("Livros disponiveís: ")
        for i, livro in enumerate(self.livros, start=1):
            print(f"{i} - {livro.titulo}")

    #método para pegar um livro pelo índice
    def selecionar_livro(self, indice):
        return self.livros[indice -1] 
        #-1 porque a lista começa em 0


#criar livros
biblioteca = Biblioteca()
titulos = ["livro1", "livro2"]

#for para add varios livros
for i in titulos:
    biblioteca.add_livro(Livro(i))

#listar
biblioteca.listar()

#nome do solicitante
nome = input("Nome para o empréstimo: ")
#pedir para escolher o livro
escolha = int(input("Digite o número do livro que deseja: "))
livro_escolhido = biblioteca.selecionar_livro(escolha)
#mostrar a confirmação
print(f"""
    Nome: {nome}
    Livro: {livro_escolhido.titulo}
""")