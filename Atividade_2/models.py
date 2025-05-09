from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional


class EstadoItem(str, Enum):
    disponivel = "disponivel"
    emprestado = "emprestado"

class Livro(BaseModel):
    id: str
    titulo: str
    autor: str
    ano_publicacao: date
    disponibilidade: EstadoItem


class Cliente(BaseModel):
    id: str
    nome: str

class Emprestimo(BaseModel):
    id: int
    user_id: str  
    livro_id: str  
    data_emprestimo: date
    data_devolucao: Optional[date] = None  

class Devolucao(BaseModel):
    id: int  
    user_id: str
    livro_id: str
    data_devolucao: date
