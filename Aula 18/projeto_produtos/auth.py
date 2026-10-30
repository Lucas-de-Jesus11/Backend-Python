# auty.py
#pip install python-jose passlib
# jose javascript object signing and encryption 
from datetime import datetime, timedelta
# datetime = ano, mes, dia, horam minuto, segundo
# timedelta = adição ou subtração de tempo ou data 

from jose import JWSError, jwt
# jwterro = erro de criptografia
# jwt = json web token = assinatura criptografada entre duas partes

from passlib.context import CryptContext
# implementação de contexto de criptografia , verificar o hash da 
# criar a chave secreta do token(em produção guardar em uma variavel)
SECRET_KEY = "chave-secreta"
ALGORITHM =  "HS256"

'''
HS256 algoritmo de criptografia de 256 bits vai criar um hash
'chave-secreta', a mesma chave é usada para assinar o jwt e 
verificar assinatura do cliente
'''

ACCESS_TOKEN_MINUTES = 30 #token de tempo de acesso - 30 minutos
#criptografia de senha 
pwd_context = CryptContext(schemes=["bcrypy"], 
                           deprecated="auto")

#funçõs de criar hash da senha
def gerar_hash_senha(senha:str):
    return pwd_context.hash(senha)

#verificar_senha
def verificar_senha(senha:str, senha_hash:str):
    return pwd_context.verify(senha, senha_hash) 

#criar token
def criar_token(dados:dict):
    dados_token = dados.copy()
    expira = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_MINUTES)
    dados_token.update({"exp":expira})
    token_jwt = jwt.encode(dados_token, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

#verificar token payload=carga útil
def verificar_token(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWSError:
        return None