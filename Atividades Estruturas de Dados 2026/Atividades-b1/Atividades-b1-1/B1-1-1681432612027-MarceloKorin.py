'''
---------------------------------------------------------
                Fatec São Caetano do Sul 
                    Atividade B1-1 
               Autor: Marcelo Enrique Korin 
                Objetivo: Trabalhar Python 
                    Data: 24/02/2026 
---------------------------------------------------------
'''

catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    if id_filme in catalogo:
        print("Filme já está cadastrado.")
    else:
        catalogo[id_filme] = {"titulo": titulo, "diretor": diretor}
        print("Filme cadastrado com sucesso.")

def buscar_filme(id_filme):
    return catalogo.get(id_filme, "Filme não localizado.")

def remover_filme(id_filme):
    catalogo.pop(id_filme, None)
    print ("Filme removido.")

def listar_todos():
    if not catalogo:
        print("\nO catálogo está vazio.")
    else:
        print ("\n- - - Listagem de Filmes ---")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Titulo: {dados['titulo']} | Diretor: {dados['diretor']}")


# --- Testes de Funcionamento ---
adicionar_filme("1", "O Poderoso Chefão", "Francis Ford Coppola")
adicionar_filme("2", "Matrix", "Lana e Lilly Wachowski")
adicionar_filme("3", "O Senhor dos Anéis: A Sociedade do Anel", "Peter Jackson")
listar_todos()  
print(buscar_filme("2"))
remover_filme("1")
listar_todos()