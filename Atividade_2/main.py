from fastapi import FastAPI, HTTPException
from models import Livro, Cliente, Emprestimo, Devolucao, EstadoItem
from typing import List

app = FastAPI(title="Bibliotequinhazinha")

livros:List[Livro]=[]
clientes:List[Cliente]=[]
emprestimos:List[Emprestimo]=[]
devolucoes:List[Devolucao]=[]

@app.get("/biblioteca/",response_model=List[Livro])
def listar_livros():
    return livros

@app.get("/biblioteca/{id}", response_model=Livro)
def listar_livro(id: str):
    for livro in livros:
        if livro.id == id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")


@app.post("/biblioteca/", response_model=Livro)
def criar_livro(livro: Livro):
    livros.append(livro)
    return livro


@app.get("/clientes/",response_model=List[Cliente])
def listar_clientes():
    return clientes

@app.post("/clientes/", response_model=Cliente)
def criar_cliente(cliente: Cliente):
    clientes.append(cliente)
    return cliente

@app.post("/emprestimos/", response_model=Emprestimo)
def registra_emprestimo(emprestimo: Emprestimo):
    cliente = next((c for c in clientes if c.id == emprestimo.user_id), None)
    livro = next((l for l in livros if l.id == emprestimo.livro_id), None)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    if livro.disponibilidade == EstadoItem.emprestado:
        raise HTTPException(status_code=400, detail="Livro já emprestado")

    livro.disponibilidade = EstadoItem.emprestado
    emprestimos.append(emprestimo)
    return emprestimo


@app.post("/devolucoes/", response_model=Devolucao)
def registra_devolucao(devolucao: Devolucao):
    cliente = next((c for c in clientes if c.id == devolucao.user_id), None)
    livro = next((l for l in livros if l.id == devolucao.livro_id), None)

    if not cliente or not livro:
        raise HTTPException(status_code=404, detail="Cliente ou livro não encontrado")

    livro.disponibilidade = EstadoItem.disponivel

    devolucoes.append(devolucao)
    return devolucao


@app.get("/clientes/{id}/livros_emprestados", response_model=List[Livro])
def exibe_livros_emprestados(id: str):
    cliente = next((c for c in clientes if c.id == id), None)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    emprestimos_ativos = [
        e for e in emprestimos
        if e.user_id == id and not any(d for d in devolucoes if d.livro_id == e.livro_id)
    ]

    livros_emprestados = [
        next((l for l in livros if l.id == e.livro_id), None)
        for e in emprestimos_ativos
    ]

    return [livro for livro in livros_emprestados if livro is not None]
