from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def teste_api():
    return{'hello':'Ola, mundo'}