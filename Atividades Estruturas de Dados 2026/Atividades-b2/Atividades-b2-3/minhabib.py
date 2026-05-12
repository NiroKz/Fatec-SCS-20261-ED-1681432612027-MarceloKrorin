'''
---------------------------------------------------------
                Fatec São Caetano do Sul 
                    Atividade B2-3
               Autor: Marcelo Enrique Korin 
                    Data: 12/05/2026 
---------------------------------------------------------
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def analisar_arvore(self, valor_busca):
        print("=" * 45)
        print("         DIAGNÓSTICO GERAL DA ÁRVORE")
        print("=" * 45)

        if self.raiz is None:
            print("Árvore vazia.")
            return

        print(f"Raiz: {self.raiz.valor}")

        print("\nNós Internos:")
        self.imprimir_nos_internos()

        print("\nNós Folha (externos):")
        self.imprimir_folhas()

        print("\nExibição por Níveis:")
        self.imprimir_niveis()

        print("=" * 45)
        print(f"   DIAGNÓSTICO ESPECÍFICO - Nó: {valor_busca}")
        print("=" * 45)

        no = self.raiz
        while no and no.valor != valor_busca:
            no = no.esq if valor_busca < no.valor else no.dir

        if no is None:
            print(f"Valor {valor_busca} não encontrado na árvore.")
            return

        grau = (1 if no.esq else 0) + (1 if no.dir else 0)
        print(f"Grau do nó {valor_busca}: {grau}")

        print(f"Ancestrais de {valor_busca}:")
        self.imprimir_ancestrais(valor_busca)

        print(f"Descendentes de {valor_busca}:")
        self.imprimir_descendentes(valor_busca)

        altura = self.calcular_altura(no)
        profundidade = self.calcular_profundidade(valor_busca)
        print(f"Altura do nó {valor_busca}: {altura}")
        print(f"Profundidade do nó {valor_busca}: {profundidade}")
        print("=" * 45)

    def imprimir_nos_internos(self, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return
        if no.esq is not None or no.dir is not None:
            print(f"  {no.valor}")
        self.imprimir_nos_internos(no.esq)
        self.imprimir_nos_internos(no.dir)

    def imprimir_folhas(self, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return
        if no.esq is None and no.dir is None:
            print(f"  {no.valor}")
        self.imprimir_folhas(no.esq)
        self.imprimir_folhas(no.dir)

    def imprimir_niveis(self):
        if self.raiz is None:
            return
        fila = [(self.raiz, 0)]
        nivel_atual = 0
        nos_nivel = []
        while fila:
            no, nivel = fila.pop(0)
            if nivel != nivel_atual:
                print(f"  Nível {nivel_atual}: {nos_nivel}")
                nos_nivel = []
                nivel_atual = nivel
            nos_nivel.append(no.valor)
            if no.esq:
                fila.append((no.esq, nivel + 1))
            if no.dir:
                fila.append((no.dir, nivel + 1))
        print(f"  Nível {nivel_atual}: {nos_nivel}")

    def calcular_altura(self, no):
        if no is None:
            return -1
        return 1 + max(self.calcular_altura(no.esq), self.calcular_altura(no.dir))

    def calcular_profundidade(self, valor, no="raiz", profundidade=0):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return -1
        if no.valor == valor:
            return profundidade
        if valor < no.valor:
            return self.calcular_profundidade(valor, no.esq, profundidade + 1)
        return self.calcular_profundidade(valor, no.dir, profundidade + 1)

    def imprimir_ancestrais(self, valor, no="raiz", ancestrais=None):
        if no == "raiz":
            no = self.raiz
            ancestrais = []
        if no is None:
            return False
        if no.valor == valor:
            print(f"  {' -> '.join(str(a) for a in ancestrais)}" if ancestrais else "  (nenhum - é a raiz)")
            return True
        ancestrais.append(no.valor)
        if self.imprimir_ancestrais(valor, no.esq, ancestrais):
            return True
        if self.imprimir_ancestrais(valor, no.dir, ancestrais):
            return True
        ancestrais.pop()
        return False

    def imprimir_descendentes(self, valor, no="raiz", encontrado=False):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return
        if no.valor == valor:
            self.imprimir_descendentes(valor, no.esq, True)
            self.imprimir_descendentes(valor, no.dir, True)
            return
        if encontrado:
            print(f"  {no.valor}")
        self.imprimir_descendentes(valor, no.esq, encontrado)
        self.imprimir_descendentes(valor, no.dir, encontrado)