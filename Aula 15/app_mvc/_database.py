#definir o servidor de banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
##conexão com sqlite
engine = create_engine("sqlite:///usuarios_z.db", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)#index para o streamlit
    email = Column(String, index=True)

#Criar tabelas no banco
Base.metadata.create_all(bind=engine)