'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul *
* Autor: Marcelo Enrique Korin *
* Desenvolver uma calculadora que utilize pilhas e a Notação Polonesa Reversa (RPN). *
* data: 30/03/2026 *
*---------------------------------------------------------*
'''
def empilhar_valor(stack_numerica, valor):
    stack_numerica.pop(0)
    stack_numerica.append(valor)

def executar_operacao(stack_numerica, operador):
    operando2 = stack_numerica.pop()
    operando1 = stack_numerica.pop()
    
    if operador == "+":
        resultado = operando1 + operando2
    elif operador == "-":
        resultado = operando1 - operando2
    elif operador == "*":
        resultado = operando1 * operando2
    elif operador == "/":
        resultado = operando1 / operando2
    else:
        print("Erro: operador inválido")
        return
    
    topo = stack_numerica[0]
    stack_numerica.insert(0, topo)
    stack_numerica.append(resultado)

def exibir_stack(stack_numerica):
    t = stack_numerica[0]
    z = stack_numerica[1]
    y = stack_numerica[2]
    x = stack_numerica[3]

    print(f"T: {t}")
    print(f"Z: {z}")
    print(f"Y: {y}")
    print(f"X: {x}")
    print("--------")

entrada_rpn = input("Digite a expressão RPN: ")
stack_numerica = [0, 0, 0, 0]
stack_expressao = []

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
            break

        executar_operacao(stack_numerica, token)

        exp2 = stack_expressao.pop()
        exp1 = stack_expressao.pop()

        nova_expressao = f"({exp1} {token} {exp2})"
        stack_expressao.append(nova_expressao)

        exibir_stack(stack_numerica)

if len(stack_expressao) > 1:
    print("Erro: operadores insuficientes")
elif len(tokens) < 2:
    print("Erro: expressão inválida")
else:
    print(f"Expressão: {nova_expressao}")
    print(f"Resultado: {stack_numerica[3]}")
