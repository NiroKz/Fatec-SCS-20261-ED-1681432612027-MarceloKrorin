'''
---------------------------------------------------------
                Fatec São Caetano do Sul 
                    Atividade B2-2
               Autor: Marcelo Enrique Korin 
                Objetivo: Treinar Filas
                    Data: 28/04/2026 
---------------------------------------------------------
'''
from collections import deque

class SistemaFilaImpressora:
    def __init__(self):
        self.entrada_aluno = []
        self.entrada_adm = []
        self.fila_reorganizada = deque()

    def adicionar(self, nome, tipo):
        if tipo == '1':
            self.entrada_aluno.append(nome)
            print(f"Aluno {nome} adicionado a espera.")
        elif tipo == '2':
            self.entrada_adm.append(nome)
            print(f"ADM {nome} adicionado a espera.")
        else:
            print("Tipo invalido.")

    def reorganizar_prioridade(self):
        if len(self.fila_reorganizada) > 0:
            print("Acao bloqueada! A fila atual ainda nao foi totalmente consumida.")
            return

        if not self.entrada_adm and not self.entrada_aluno:
            print("Nao ha ninguem nas listas de espera para organizar.")
            return

        novos_adms = [f"{n} (ADM)" for n in self.entrada_adm]
        novos_alunos = [f"{n} (ALUNO)" for n in self.entrada_aluno]
        
        self.fila_reorganizada = deque(novos_adms + novos_alunos)
        
        self.entrada_adm.clear()
        self.entrada_aluno.clear()
        print("Nova fila de impressao gerada com sucesso!")

    def consumir(self):
        if self.fila_reorganizada:
            pessoa = self.fila_reorganizada.popleft()
            print(f"Processando impressao para: {pessoa}")
        else:
            print("Fila vazia. Adicione pessoas e reorganize para imprimir.")

    def listar_status(self):
        print("\n" + "------------------------------------------------------")
        print(f"Espera ADM: {self.entrada_adm}")
        print(f"Espera ALUNO: {self.entrada_aluno}")
        print(f"FILA DE IMPRESSAO ATUAL: {list(self.fila_reorganizada)}")
        print("------------------------------------------------------")

sistema = SistemaFilaImpressora()

while True:
    print("\n--- CONTROLE DE FILA ---")
    print("1. Adicionar Nome")
    print("2. Reorganizar")
    print("3. Consumir Proximo")
    print("4. Listar Tudo")
    print("5. Sair")
    
    opcao = input("Opcao: ")

    if opcao == '1':
        nome = input("Nome da pessoa: ")
        tipo = input("Tipo (1-Aluno, 2-ADM): ")
        sistema.adicionar(nome, tipo)
    elif opcao == '2':
        sistema.reorganizar_prioridade()
    elif opcao == '3':
        sistema.consumir()
    elif opcao == '4':
        sistema.listar_status()
    elif opcao == '5':
        break
    else:
        print("Opcao invalida!")
