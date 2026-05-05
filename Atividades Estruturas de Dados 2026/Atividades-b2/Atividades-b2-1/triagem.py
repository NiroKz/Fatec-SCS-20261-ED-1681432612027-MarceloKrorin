#/-----------------------------------------------------------------------------------------/
#/*                         FATEC-São Caetano do Sul                                        */
#/*                         Estrutura de Dados                                              */
#/*                         Id da Atividade: B2-1                                           */
#/*             Objetivo: Manupular filas para criar uma ordem de prioridade para pacientes */
#/*            Autor: ERICK JOSHUA REVOLLO, GABRIEL XAVIER DE ALMEIDA                       */
#/*                          E MARCELO ENRIQUE KORIN                                        */
#/*                            Data:04/05/2026                                              */
#/-----------------------------------------------------------------------------------------/

from ListaPacientes import fila_bruta

PALAVRAS_EMERGENCIA = ["dor no peito", "falta de ar", "inconsciente"]

def calcular_prioridade(paciente):
    sintoma = paciente.sintoma_relatado.lower()

    if "inconsciente" in sintoma:
        nivel = 1
    elif "dor no peito" in sintoma or "falta de ar" in sintoma:
        nivel = 2
    elif any(p in sintoma for p in PALAVRAS_EMERGENCIA):
        nivel = 3
    elif paciente.idade >= 60 or paciente.pcd == "s" or paciente.gestante == "s":
        nivel = 4
    else:
        nivel = 5

    bonus = 0 if (paciente.pcd == "s" or paciente.gestante == "s" or paciente.idade >= 60) else 1

    return (nivel, bonus, paciente.timestamp_chegada)


def classificar_e_ordenar(fila):
    for paciente in fila:
        nivel, _, _ = calcular_prioridade(paciente)
        paciente.nivel_prioridade = nivel

        sintoma = paciente.sintoma_relatado.lower()
        paciente.emergencia = any(p in sintoma for p in PALAVRAS_EMERGENCIA)

    return sorted(fila, key=calcular_prioridade)


fila_ordenada = classificar_e_ordenar(fila_bruta)

print("\n" + "=" * 60)
print("  ORDEM DE ATENDIMENTO")
print("=" * 60)
for paciente in fila_ordenada:
    print(paciente)
print("=" * 60)