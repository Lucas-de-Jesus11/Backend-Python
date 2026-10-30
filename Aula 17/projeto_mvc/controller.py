'''
api router para ligar o backend com frontend
criar uma rota da api para redirecionar para o html
'''
#import api rota, redirecionar para o html
from fastapi import APIRouter, Depends, Request, Form

#Request = requisição http// Depends é o método GET,POST,PUT,DELETE

#import conexão do ORM
from sqlalchemy.orm import Session

#import conexão com o database usuarios sqlite
from database import SessionLocal

#import do models manipulação nome e email do usuario
from models import SessionLocal, Usuario

#import resposta do html método http
from fastapi.responses import HTMLResponse, RedirectResponse

#motor gráfico do template, renderizar html,css,javascript
#pip install jinja2
from fastapi.templating import Jinja2Templates

#criar uma variavel responsavel pelas rotas
router=APIRouter()

#configurar o template do frontend
templates = Jinja2Templates(directory="views")#pasta do html

#função para abrir e fechar sessão com banco de dados
def get_db():
    db = SessionLocal()#conexão com o banco de dados sqlite
    try:
        yield db #yield coletar o banco de dados
    finally:
        db.close()#finaliza a função, fechando a conexão

#rota inicial(redirecionar o get da api para o index.html)
@router.get("/", response_class=HTMLResponse)
#função para fazer request na api trazer os dados do banco e
#redirecionar para o html 'frontend'
async def home(request: Request, db:Session=Depends(get_db)):
    #buscar todos os usuarios do banco de dados
    usuarios = db.query(Usuario).all()
    #retorna os dados para a página html 'index.html'
    return templates.TemplateResponse("index.html", {
        "request":request, "usuarios":usuarios
    })

#rota: formulário de novo usuario
@router.get("/novo", response_class=HTMLResponse)
async def novo_usuario(request:Request):
    return templates.TemplateResponse("novo.html", {"request":request})

#rota post criar usuario(POST)
@router.post("/criar")
async def criar_usuario(nome:str=Form(...), email:str=Form(...), 
    db:Session=Depends(get_db)):
    usuario = Usuario(nome=nome, email=email)
    db.add(usuario)
    db.commit()
    return RedirectResponse(url="/", status_code=303)#303 código http redirecionamento de página

#rota formulário de edição
@router.get("/editar/{usuario_id}", response_class=HTMLResponse)
async def editar_usuario(usuario_id:int, request:Request,
                         db:Session=Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id==usuario_id).first()
    return templates.TemplateResponse("editar.html",
                                      {"request":request, "usuario":usuario})

@router.post("/atualizar/{usuario_id}")
async def atualizar_usuario(usuario_id:int, nome:str=Form(...), email:str=Form(...), 
    db:Session=Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id==usuario_id).first()
    usuario.nome=nome
    usuario.email=email
    db.commit()
    return RedirectResponse(url="/", status_code=303)