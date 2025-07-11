import requests

URL = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{URL}/livros")
    if r.status_code == 200:
        print(r.text)

def cadastrar_livros():
    titulo = input("\nDigite o título: ")
    ano = int(input("Digite o ano: "))
    edicao = float(input("Digite a edição: "))
    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }
    requests.post(f"{URL}/livros", json=livro)

def listar_livro(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def excluir_livro(titulo):
    r = requests.delete(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print("Excluído com sucesso!")
    else:
        print(r.text)

def menu():
    print("\n1 - Listar Livros")
    print("2 - Listar Livros pelo titulo")
    print("3 - Cadastrar Livros")
    print("4 - Excluir Livros")
    print("5 - Sair\n")
    return int(input("Digite sua opção: "))

opcao = menu()

while opcao != 5:
    if opcao == 1:
        listar_livros()
    elif opcao == 2:
        titulo = input("\nDigite o titulo: ")
        listar_livro(titulo)
    elif opcao == 3:
        cadastrar_livros()
    elif opcao == 4:
        titulo = input("\nDigite o titulo: ")
        excluir_livro(titulo)
    else:
        print("\nColoque um número válido!\n")
    opcao = menu()

