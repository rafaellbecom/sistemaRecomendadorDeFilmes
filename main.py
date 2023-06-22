from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from recomendacao import *


app = FastAPI()
recomendation = None

# Configuração do CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:5500"
    # Adicione aqui as origens permitidas (URLs) para acesso à sua API
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class User(BaseModel):
    user_name: str

@app.post('/')
def sendUser(user:User):
    base = carregaMovieLens()  
    global recomendation
    recomendation = getRecomendacoesUsuario(base, user.user_name)
    return recomendation


@app.get('/')
def getRecomendations():
    global recomendation

    return {
        'recomendations': recomendation
    }