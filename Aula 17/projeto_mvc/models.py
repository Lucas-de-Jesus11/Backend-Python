from sqlalchemy import Column, Integer, String

#import conexão com sqlite
from database import Base, engine, SessionLocal

#criar o modelo para o usuário
class Usuario(Base):
    __tablename__  = "usuarios" #nome da tabela
    #colunas da tabela
    id = Column(Integer, primary_key=True, index=True)#index para o html
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)#unique para email@plataforma

#teste criar tabela no banco de dados
#Base.metadata.create_all(bind=engine)

#função para criar um usuário teste
def criar_user(nome:str, email:str):
    session = SessionLocal()
    usuario = Usuario(nome=nome, email=email)
    session.add(usuario)
    session.commit()
#criar o user teste
# criar_user("User-teste3", "teste3@gmail.com")