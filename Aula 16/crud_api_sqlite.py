#crud api sqlite
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="API itens com sqlite")
#nome do banco
BANCO = "itens.db"
#criar tabelas no sqlite
def criar_tabela():
    conn = sqlite3.connect(BANCO)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome  TEXT NOT NULL,
                price REAL NOT NULL,
                quantidade INTEGER NOT NULL)""")
    conn.commit()
    conn.close()
#criar_tabela()

#teste criar um dado


#modelo pydantic do item
class Item(BaseModel):
    nome:str
    price: float
    quantidade: int
#endpoint para listar todos os itens(GET)
@app.get("/")
async def listar_itens():
    conn = sqlite3.connect(BANCO)
    cur = conn.cursor()
    cur.execute("SELECT * FROM itens")
    linhas = cur.fetchall()
    return {"itens":linhas}

#endpoint para pegar o item pelo id (GET)
@app.get("/items/{item_id}")
async def get_item(item_id:int):
    conn = sqlite3.connect(BANCO)
    cur = conn.cursor()
    cur.execute("SELECT * FROM itens WHERE id=?",
                (item_id,))
    item = cur.fetchall()
    if item:
        return{"item":item}
    return{"ERRO":"Item não encontrado"}

#endpoint para pegar o item pelo nome (GET)
@app.get("/items-nome/{item_nome}")
async def get_item(item_nome:str):
    conn = sqlite3.connect(BANCO)
    cur = conn.cursor()
    cur.execute("SELECT * FROM itens WHERE nome=?",
                (item_nome,))
    item = cur.fetchall()
    if item:
        return{"item":item}
    return{"ERRO":"Item não encontrado"}

#criar item(post)
@app.post("/items-criar/")
async def get_item(item:Item):
    conn = sqlite3.connect(BANCO)
    cur = conn.cursor()
    cur.execute("""INSERT INTO itens(
                nome, price, quantidade)
                VALUES (?,?,?)""",
                (item.nome, item.price, item.quantidade))
    conn.commit()
    item_id = cur.lastrowid#criar o item na ultima linha
    return{"id":item_id, "mensagem":"Item criado"}

#endpoint put atualizar
@app.put("/items-atualizar/{item_id}")
async def update_item(item_id:int, item:Item):
    conn = sqlite3.connect(BANCO)
    cur = conn.cursor()
    cur.execute("""UPDATE itens SET nome=?, price=?, quantidade=?
                WHERE id=?""",
                (item.nome, item.price, item.quantidade, item_id))
    conn.commit()
    atualizado = cur.rowcount#contar a linha para atualizar na posição
    if atualizado:
        return{"mensagem":f"Item{item_id} atualizado"}
    return {"Erro":"Item não atualizado"}

#endpoint delete deletar dados
@app.delete("/items-deletar/{item_id}")
async def deletar_item(item_id:int, item:Item):
    conn = sqlite3.connect(BANCO)
    cur = conn.cursor()
    cur.execute("""DELETE FROM itens WHERE id=?""",
                (item_id,))
    conn.commit()
    deletar = cur.rowcount#contar a linha para atualizar na posição
    if deletar:
        return{"mensagem":f"Item{item_id} deletado"}
    return {"Erro":"Item não deletado"}
