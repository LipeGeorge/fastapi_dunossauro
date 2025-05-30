from typing import List

from fastapi import APIRouter

from Praticas_sala.ApiBlog.schemas import Usuario

router = APIRouter()


@router.get('/', response_model=List[Usuario])
def listar_usuarios(): ...
