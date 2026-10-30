#import do database.py - conexão com sqlite
from _database import * #Base
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)#index para o streamlit
    email = Column(String, index=True)

