#ordem do padrão mvc
'''
1- definir conexão com banco de dados sqlite- database.py
2- definir o modelo ORM - tabela usuarios, id, nome e email
3- regras de negócio e rotas do back-end- controller.py
4- template da aplicação view front-end- index.html
5- ponto de saida da aplicação, subir a aplicação- main.py
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#criar a conexão com o banco de dados sqlite nome database
DATABASE_URL = "sqlite:///./meubanco.db"

#engine do banco
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#criar sessão do banco de dados para consultas de usuários
SessionLocal = sessionmaker(bind=engine)

#classe base para os models
Base = declarative_base()