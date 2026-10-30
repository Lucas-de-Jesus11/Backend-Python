#aula17 rotas fake fastapi
from fastapi import FastAPI
from pydantic import BaseModel
#criar a instancia da api
app = FastAPI(title="Rotas fake API")
#endpoint simples para teste da api
@app.get("/")
async def teste_api():
    return{"mensagem": "Teste get api"}
#rodar api #pasta do arquivo da api
#python -m uvicorn nome_arquivo:app --reload
#produtos fake para teste
produtos = {
    1:{"nome":"caneta","price":2.55,"quantidade":100},
    2:{"nome":"lapis","price":1.55,"quantidade":100},
    3:{"nome":"borracha","price":0.55,"quantidade":100},
}
#endpoint produtos
@app.get("/get-produtos")
async def get_produto():
    return produtos

#endpoint produtos pelo id path parameter
@app.get("/get-produtos/{id_produto}")
async def produtos_id(id_produto:int):
    return produtos[id_produto]

#endpoint produtos pelo nome query parameter
@app.get("/get-produto-nome")
async def get_produto_nome(nome:str):
    for i in produtos:#loop para rodar os dados 
        if produtos[i]["nome"]==nome:#retorna nome se for igual
            return produtos[i]#retorna o produto pelo index
    return {"DADOS":"Produto não encontrado"}

class Item(BaseModel):
    nome:str
    price: float
    quantidade: int

@app.post("/items/")
async def criar_item(item:Item):
    return {"item":item}

@app.put("/items-update/{item_id}")
async def update_item(item_id:int, item:Item):
    return {"item_id":item_id,"update_item":item}

@app.delete("/items-deletar/{item_id}")
async def deletar_item(item_id:int):
    return {"mensagem":f"Item {item_id} deletado"}