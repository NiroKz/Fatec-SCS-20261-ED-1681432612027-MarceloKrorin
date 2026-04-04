'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul *
* Autores: Erick Joshua Revollo, Gabriel Xavier de Almeida e Marcelo Enrique Korin *
* Desenvolver uma calculadora que utilize pilhas e a Notação Polonesa Reversa (RPN). *
* data: 31/03/2026 *
*---------------------------------------------------------*
'''

def empilhar_valor(stack_numerica, valor):
    if stack_numerica[3] == 0:
        stack_numerica[3] = valor
    elif stack_numerica[2] == 0:
        stack_numerica[2] = valor
    elif stack_numerica[1] == 0:
        stack_numerica[1] = valor
    elif stack_numerica[0] == 0:
        stack_numerica[0] = valor
    else:
        stack_numerica[3] = stack_numerica[2]
        stack_numerica[2] = stack_numerica[1]
        stack_numerica[1] = stack_numerica[0]
        stack_numerica[0] = valor


def executar_operacao(stack_numerica, operador):
    ocupados = []
    for i in range(3, -1, -1): 
        if stack_numerica[i] != 0:
            ocupados.append(i)
    
    if len(ocupados) < 2:
        print("Erro: operandos insuficientes")
        return False

    idx_topo = ocupados[-1]      
    idx_anterior = ocupados[-2]  

    operando_topo = stack_numerica[idx_topo]
    operando_anterior = stack_numerica[idx_anterior]

    if operador == "+":
        resultado = operando_anterior + operando_topo
    elif operador == "-":
        resultado = operando_anterior - operando_topo
    elif operador == "*":
        resultado = operando_anterior * operando_topo
    elif operador == "/":
        if operando_topo == 0:
            print("Erro: divisão por zero")
            return False
        resultado = operando_anterior / operando_topo
    else:
        return False

    stack_numerica[idx_anterior] = resultado
    stack_numerica[idx_topo] = 0

    return True


def exibir_stack(stack_numerica):
    print(f"T: {stack_numerica[0]}")
    print(f"Z: {stack_numerica[1]}")
    print(f"Y: {stack_numerica[2]}")
    print(f"X: {stack_numerica[3]}")
    print("--------")


entrada_rpn = input("Digite a expressão RPN: ")

stack_numerica = [0, 0, 0, 0]
stack_expressao = []
erro = False

tokens = entrada_rpn.split()

for token in tokens:
    try:
        numero = float(token)
        empilhar_valor(stack_numerica, numero)
        stack_expressao.append(str(numero))
        exibir_stack(stack_numerica)

    except ValueError:
        if len(stack_expressao) < 2:
            print("Erro: operandos insuficientes")
            erro = True
            break

        sucesso = executar_operacao(stack_numerica, token)
        if not sucesso:
            erro = True
            break

        exp2 = stack_expressao.pop()
        exp1 = stack_expressao.pop()

        nova_expressao = f"({exp1} {token} {exp2})"
        stack_expressao.append(nova_expressao)

        exibir_stack(stack_numerica)

if not erro:
    if len(tokens) < 1:
        print("Erro: expressão inválida")
    elif len(stack_expressao) > 1:
        print("Erro: operadores insuficientes")
    else:
        print(f"Expressão: {stack_expressao[0]}")
        print(f"Resultado: {stack_numerica[3]}")
