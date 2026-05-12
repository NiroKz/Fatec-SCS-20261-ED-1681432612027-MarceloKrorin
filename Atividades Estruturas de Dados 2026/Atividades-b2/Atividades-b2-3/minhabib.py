'''
---------------------------------------------------------
                Fatec São Caetano do Sul 
                    Atividade B2-3
               Autor: Marcelo Enrique Korin 
                    Data: 12/05/2026 
---------------------------------------------------------
'''
def analisar_arvore(raiz, valor_busca):
    print("=" * 45)
    print("         DIAGNÓSTICO GERAL DA ÁRVORE")
    print("=" * 45)

    if raiz is None:
        print("Árvore vazia.")
        return

    print(f"Raiz: {raiz['valor']}")

    print("\nNós Internos:")
    imprimir_nos_internos(raiz)

    print("\nNós Folha (externos):")
    imprimir_folhas(raiz)

    print("\nExibição por Níveis:")
    imprimir_niveis(raiz)

    print("=" * 45)
    print(f"   DIAGNÓSTICO ESPECÍFICO - Nó: {valor_busca}")
    print("=" * 45)

    # Busca do nó
    no_atual = raiz
    while no_atual and no_atual["valor"] != valor_busca:
        no_atual = no_atual["esq"] if valor_busca < no_atual["valor"] else no_atual["dir"]

    if no_atual is None:
        print(f"Valor {valor_busca} não encontrado na árvore.")
        return

    grau = (1 if no_atual["esq"] else 0) + (1 if no_atual["dir"] else 0)
    print(f"Grau do nó {valor_busca}: {grau}")

    print(f"Ancestrais de {valor_busca}:")
    imprimir_ancestrais(raiz, valor_busca)

    print(f"Descendentes de {valor_busca}:")
    imprimir_descendentes(raiz, valor_busca)

    altura = calcular_altura(no_atual)
    profundidade = calcular_profundidade(raiz, valor_busca)
    print(f"Altura do nó {valor_busca}: {altura}")
    print(f"Profundidade do nó {valor_busca}: {profundidade}")
    print("=" * 45)

def imprimir_nos_internos(no):
    if no is None:
        return
    if no["esq"] is not None or no["dir"] is not None:
        print(f"  {no['valor']}")
    imprimir_nos_internos(no["esq"])
    imprimir_nos_internos(no["dir"])

def imprimir_folhas(no):
    if no is None:
        return
    if no["esq"] is None and no["dir"] is None:
        print(f"  {no['valor']}")
    imprimir_folhas(no["esq"])
    imprimir_folhas(no["dir"])

def imprimir_niveis(raiz):
    if raiz is None:
        return
    fila = [(raiz, 0)]
    nivel_atual = 0
    nos_nivel = []
    while fila:
        no, nivel = fila.pop(0)
        if nivel != nivel_atual:
            print(f"  Nível {nivel_atual}: {nos_nivel}")
            nos_nivel = []
            nivel_atual = nivel
        nos_nivel.append(no["valor"])
        if no["esq"]:
            fila.append((no["esq"], nivel + 1))
        if no["dir"]:
            fila.append((no["dir"], nivel + 1))
    print(f"  Nível {nivel_atual}: {nos_nivel}")

def calcular_altura(no):
    if no is None:
        return -1
    return 1 + max(calcular_altura(no["esq"]), calcular_altura(no["dir"]))

def calcular_profundidade(no, valor, profundidade=0):
    if no is None:
        return -1
    if no["valor"] == valor:
        return profundidade
    if valor < no["valor"]:
        return calcular_profundidade(no["esq"], valor, profundidade + 1)
    return calcular_profundidade(no["dir"], valor, profundidade + 1)

def imprimir_ancestrais(no, valor, ancestrais=None):
    if ancestrais is None:
        ancestrais = []
    if no is None:
        return False
    if no["valor"] == valor:
        print(f"  {' -> '.join(str(a) for a in ancestrais)}" if ancestrais else "  (nenhum - é a raiz)")
        return True
    ancestrais.append(no["valor"])
    if imprimir_ancestrais(no["esq"], valor, ancestrais):
        return True
    if imprimir_ancestrais(no["dir"], valor, ancestrais):
        return True
    ancestrais.pop()
    return False

def imprimir_descendentes(no, valor, encontrado=False):
    if no is None:
        return
    if no["valor"] == valor:
        imprimir_descendentes(no["esq"], valor, True)
        imprimir_descendentes(no["dir"], valor, True)
        return
    if encontrado:
        print(f"  {no['valor']}")
    imprimir_descendentes(no["esq"], valor, encontrado)
    imprimir_descendentes(no["dir"], valor, encontrado)