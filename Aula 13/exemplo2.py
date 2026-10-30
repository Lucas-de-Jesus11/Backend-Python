from sqlalchemy import create_engine, Column, Integer, String, Float
#create engine= função cria uma instancia de forma padrão
#Column = Coluna na tabela do banco de dados
#Interger=tipo int inteiro no banco de dados
#String-str texto é o varchar do database
#Float-tipo float real para database

from sqlalchemy.ext.declarative import declarative_base
#sqlalchemy.ext.declarative construtor do objeto para declaração de classes
#produz os objetos do sqlalchemy para mapeamento das tabelas
#declarative_base chamar o mapeamento do orm com base nas informações fornecidas

from sqlalchemy.orm import sessionmaker
#sessionmaker configuração de sessão do banco de dados
#criar o engine para conectar ao banco de dados sqlite
engine = create_engine('sqlite:///titulo.db',echo=True)#echo vai exibir os comandos do sqlalchemy no terminal
#base para definir os modelos
Base = declarative_base()
#definir o modelo(equivalente a criar a tabela)
class Filmes(Base):
    __tablename__ = 'filmes'#nome da tabela no banco
    #atributos do objeto
    id = Column(Integer, primary_key=True, autoincrement=True)#chave primaria auto-incrementada
    nome = Column(String, nullable=False)#texto
    ano = Column(Integer, nullable=False)#inteiro
    nota = Column(Float, nullable=False)#float real
    #metodo especial para retornar os dados em string
    def __repr__(self):
        return f"Id={self.id} Nome={self.nome} Ano={self.ano} Nota={self.nota}"

#criar a tabela no banco(equivalente a CREATE TABLE)
def criar_tabela():
    Base.metadata.create_all(engine)#criar a tabela definida
    #metadata.create_all - criar as tabelas definidas e as colunas
    print("Tabela 'filmes' criada com sucesso")
#testar
#criar_tabela()
#criar a sessão(conexão temporaria)
def criar_sessao():
    Session=sessionmaker(bind=engine)
    return Session

#exercicio simples, adicionar, visualizar, atualizar e deletar
def adicionar_filme(nome, nota, ano):
    nome  = input("Digite o nome do filme: ")
    ano = int(input("Ano do filme: "))
    nota = float(input("Nota para o filme: ")) 
    filme = Filmes(nome=nome, ano=ano, nota=nota)
    session = criar_sessao()
    session.add(filme)
    session.commit()
    #print(f"Filme {nome} adicionado com sucesso!")
    

def listar_filme():
    session = criar_sessao()
    filmes = session.query(Filmes).all()
    print("Usuários cadastrados:")
    for i in filmes:
        print(i)

#def atualizar_filme():


   

criar_tabela()
adicionar_filme()
listar_filme()
#atualizar_filmes("Homem_Aranha", 2015, 8.5)