'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul *
* Exemplo de Manipulação de Lista ligada *
* Autor: Marcelo Enrique Korin *
* Objetivo:Mostrar manipulação de lista ligada em python *
* data: 09/03/2026 *
*---------------------------------------------------------*
'''
# Banco de dados em memoria (Dicionario)

def valorExite(listaCabeca, valorEntrada):
    atual = listaCabeca

    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]

    return False


# funcao de Inserir no começo
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")

    if valorExite(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": listaEntrada}

    print("Produto inserido no INICIO com sucesso")
    return novoNo


# funcao de Inserir no fim
def inserirFim(listaEntrada):
    valor = input("Digite o valor: ")

    if valorExite(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": None}

    if listaEntrada is None:
        print("Produto inserido no FIM com sucesso")
        return novoNo

    atual = listaEntrada

    while atual["proximo"] is not None:
        atual = atual["proximo"]

    atual["proximo"] = novoNo

    print("Produto inserido no FIM com sucesso")
    return listaEntrada


# funcao de Inserir no meio
def inserirMeio(listaEntrada):
    valor = input("Digite o valor: ")
    posicao = int(input("Digite a posição para inserir: "))

    if valorExite(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": None}

    if posicao == 0:
        novoNo["proximo"] = listaEntrada
        return novoNo

    atual = listaEntrada
    contador = 0

    while atual is not None and contador < posicao - 1:
        atual = atual["proximo"]
        contador += 1

    if atual is None:
        print("Posição inválida")
        return listaEntrada

    novoNo["proximo"] = atual["proximo"]
    atual["proximo"] = novoNo

    print("Produto inserido no MEIO com sucesso")
    return listaEntrada


# funcao de Listar
def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista vazia")
        return

    listaAtual = listaRecebida

    while listaAtual is not None:
        print(listaAtual["valor"], end="->")
        listaAtual = listaAtual["proximo"]

    print("None")


# funcao de Buscar
def buscar(listaRecebida):
    argumentoPesquisa = input("informe o argumento de pesquisa:")

    listaAtual = listaRecebida
    posicao = 0

    while listaAtual is not None:
        if listaAtual["valor"] == argumentoPesquisa:
            print(f"valor encontrado na posição {posicao}")
            return

        listaAtual = listaAtual["proximo"]
        posicao += 1

    print("Valor não encontrado")

# funcao de Remover
def remover(listaEntrada):
    valor = input("Digite o valor para remover: ")

    if listaEntrada is None:
        print("Lista vazia")
        return listaEntrada

    if listaEntrada["valor"] == valor:
        print("Produto removido com sucesso")
        return listaEntrada["proximo"]

    atual = listaEntrada

    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == valor:
            atual["proximo"] = atual["proximo"]["proximo"]
            print("Produto removido com sucesso")
            return listaEntrada

        atual = atual["proximo"]

    print("Valor não encontrado")
    return listaEntrada


# Exemplo de Menu de Interacao
def menu():
    lista = None

    while True:
        print("\n1-Inserir no Início")
        print("2-inserir no Fim")
        print("3-Inserir no meio")
        print("4-listar")
        print("5-remover")
        print("6-Buscar")
        print("0-Sair")

        opcao = input("Escolha uma operacao: ")

        if opcao == '1':
            lista = inserirInicio(lista)

        elif opcao == '2':
            lista = inserirFim(lista)

        elif opcao == '3':
            lista = inserirMeio(lista)

        elif opcao == '4':
            listar(lista)

        elif opcao == '5':
            lista = remover(lista)

        elif opcao == '6':
            buscar(lista)

        elif opcao == '0':
            print("Obrigado por usar o sistema")
            break

        else:
            print("**Opcao invalida**")


print("**bemvindo ao programa**")
menu()
