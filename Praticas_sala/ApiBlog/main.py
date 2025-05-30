from fastapi import FastAPI
from rotas import posts, usuarios

app = FastAPI()

app.include_router(usuarios.router, prefix='/usuarios')
app.include_router(posts.router, prefix='/feed')


@app.get('/')
def home():
    return {'message': 'Bem vindo ao Blog, Pessoal!'}
