#database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#conexão com o banco de dados
DATABASE_URL = "sqlite:///./produtos.db"

#criar engine
engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread": False
})

#Sessão 
SessionLocal = sessionmaker(bind=engine)

#Base para o models
Base = declarative_base()

#função para Dependencia para injetar sessão no fastapi
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()