from fastapi import FastAPI #framework

#import do backend
from controller import router

#iniciar o fastapi
app = FastAPI(title="Projetinho MVC com fastapi, sqlite, index html")
#incluir as rotas do controller 
app.include_router(router)

#python -m uvicorn main:app --reload
