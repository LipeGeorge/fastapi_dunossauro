from typing import List

from fastapi import APIRouter

from Praticas_sala.ApiBlog.schemas import Post

posts = APIRouter()


@posts.get('/', response_model=List[Post])
def listar_posts():
    # ler do banco de dados da coluna posts para mostrar todos.
    ...
