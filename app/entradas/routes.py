from datetime import datetime
from typing import List
from fastapi import APIRouter

from .models import Entrada
from .schemas import EntradaSchema
from app.config.db import session as db


route = APIRouter()

@route.get('/', response_model=List[EntradaSchema])
async def get_entradas(data: datetime = None) -> List[EntradaSchema]:
    """Rota responsavel por mostrar todas entradas"""
    table = db.query(Entrada)

    entradas = table.all()
    if data:
        entradas = table.filter(Entrada.data >= data).all()
    return entradas


@route.post('/', response_model=EntradaSchema)
async def add_entrada(entrada: EntradaSchema) -> EntradaSchema:
    """Rota responsável por adicionar entrada"""
    new_entrada = Entrada(**entrada.__dict__)
    db.add(new_entrada)
    db.commit()
    return entrada