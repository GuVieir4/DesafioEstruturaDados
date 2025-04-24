orientadores = {}
alunos = []

def cadastrar_orientador(nome: str, orientadores: dict):
    orientadores[nome] = []

def cadastrar_aluno(nome: str, matricula: int, orientador: str, lista):
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": []
    }
    lista.append(aluno)


def encontrar_aluno_por_matricula(matricula: int, lista):
    for aluno in lista:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def cadastrar_entrega(matricula: int, versao: str, data: str, lista):
    aluno = encontrar_aluno_por_matricula(matricula, lista)
    if aluno is not None:
        entrega = (versao, data)
        aluno["entregas"].append(entrega)
    else:
        return f"Aluno com matrícula {matricula} não encontrado."
    

def cadastrar_nota(matricula: int, nota: int, lista):
    aluno = encontrar_aluno_por_matricula(matricula, lista)
    if aluno and aluno["entregas"]:
        ultima_entrega = aluno["entregas"][-1]
        nova_entrega = (ultima_entrega[0], ultima_entrega[1], nota)
        aluno["entregas"][-1] = nova_entrega


# Testando se tá funcionando
cadastrar_orientador("Prof Teste", orientadores)
print(orientadores)
cadastrar_orientador("Prof 2", orientadores)
print(orientadores)

cadastrar_aluno("Gustavo", 19, "Prof Gustavo", alunos)
print(alunos)
cadastrar_aluno("Maria", 20, "Prof Caio", alunos)
print(alunos)

cadastrar_entrega(19, "v1", "2025-04-23", alunos)
print(alunos)
cadastrar_entrega(20, "v1", "2025-04-22", alunos)
print(alunos)

cadastrar_nota(19, 8, alunos)
print(alunos)
cadastrar_nota(20, 9, alunos)
print(alunos)   