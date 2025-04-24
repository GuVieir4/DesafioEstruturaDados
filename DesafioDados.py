orientadores = {}
alunos = []

def cadastrar_orientador(orientadores: dict):
    nome = input("Digite o nome do orientador: ")
    orientadores[nome] = []

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    orientador = input("Digite o nome do orientador do aluno: ")
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": []
    }
    alunos.append(aluno)

def encontrar_aluno_por_matricula(alunos):
    matricula = int(input("Digite a matrícula do aluno: "))
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def cadastrar_entrega(alunos):
    versao = input("Digite a versão da entrega: ")
    data = input("Digite a data da entrega (Ano/Mês/Dia): ")
    aluno = encontrar_aluno_por_matricula(alunos)
    if aluno is not None:
        entrega = (versao, data)
        aluno["entregas"].append(entrega)
    else:
        print("Aluno não encontrado.")

def cadastrar_nota(alunos):
    nota = float(input("Digite a nota: "))
    aluno = encontrar_aluno_por_matricula(alunos)
    if aluno is not None:
        aluno["nota"] = nota
    else:
        print("Aluno não encontrado.")

# Testando se tá funcionando
print("Cadastrando orientador")
cadastrar_orientador(orientadores)
print(f"Orientadores - {orientadores}")

print("Cadastrando aluno")
cadastrar_aluno(alunos)
print(f"Alunos - {alunos}")
