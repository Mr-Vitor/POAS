#pip install requests

import requests

url = "http://127.0.0.1:8000"


def listar_livros():
    r = requests.get(f"{url}/livros")
    if r.status_code == 200:
        print(r.text)

def listar_um_livro(titulo):
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print("Livro não encontrado")

def cadastrar_livro():
    titulo = input("Digite o título: ")
    ano = int(input("Digite o ano: "))
    edicao = float(input("Digite a edição: "))
    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }
    requests.post(f"{url}/livros", json=livro)

def deletar_livro(titulo):
    r = requests.delete(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        print("O livro foi excluído")
    elif r.status_code == 404:
        print("Livro não encontrado")

def editar_livro(titulo):
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        title = str(input("Digite o título: "))
        year = int(input("Digite o ano: "))
        edition = float(input("Digite a edição: "))
        livro = {
            "titulo": title,
            "ano": year,
            "edicao": edition
        }
        requests.put(f"{url}/livros/{titulo}", json=livro)
        print("Livro atualizado!")
    elif r.status_code == 404:
        print("Livro não encontrado")
    

def menu():
    print("""\n1 - Listar todos os livros
2 -  Pesquisar livro por título
3 - Cadastrar um livro
4 - Deletar um livro
5 - Editar um livro
6 - Sair\n""")
    return int(input("Selecione uma opção: "))

opcao = menu()

while opcao != 6:
    if opcao == 1:
        listar_livros()
    elif opcao == 2:
        titulo = str(input("Informe o livro p/ busca: "))
        listar_um_livro(titulo)
    elif opcao == 3:
        cadastrar_livro()
    elif opcao == 4:
        titulo = input("\nInforme o livro p/ excluir: ")
        deletar_livro(titulo)
    elif opcao == 5:
        titulo = input("\nInforme o livro p/ editar: ")
        editar_livro(titulo)
    else:
        print("\nColoque um número válido!\n")
    opcao = menu()