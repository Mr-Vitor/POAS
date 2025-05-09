from fastapi import FastAPI, HTTPException
from models import Tarefa
from typing import List

app = FastAPI()

tarefas:List[Tarefa]=[]

@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.get("/tarefas/{id}", response_model=Tarefa)
def tarefa_id(id:int):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
    raise HTTPException(status_code=404,detail="Não existe")

@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    tarefas.append(tarefa)
    return tarefa

@app.delete("/tarefas/", response_model=Tarefa)
def excluir_tarefa(tarefa:Tarefa):
    tarefas.remove(tarefa)
    return tarefa