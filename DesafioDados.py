orientadores = {}
alunos = []

# CADASTRO DE ORIENTADORES
def cadastrar_orientador():
    nome = input("Digite o nome do orientador: ")
    if nome in orientadores:
        print("Orientador já cadastrado.")
    else:
        orientadores[nome] = []
        print("Orientador cadastrado com sucesso.")

# CADASTRO DE ALUNOS
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    orientador = input("Digite o nome do orientador do aluno: ")

    if orientador not in orientadores:
        print("Erro: orientador não encontrado. Cadastre o orientador primeiro.")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula or aluno["nome"].lower() == nome.lower():
            print("Erro: aluno já cadastrado.")
            return

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": []
    }
    alunos.append(aluno)
    orientadores[orientador].append(nome)
    print("Aluno cadastrado com sucesso.")

# BUSCA DE ALUNO
def encontrar_aluno():
    metodo = input("Buscar aluno por (1) Nome ou (2) Matrícula? ")
    if metodo == "1":
        nome = input("Digite o nome do aluno: ")
        for aluno in alunos:
            if aluno["nome"].lower() == nome.lower():
                return aluno
    elif metodo == "2":
        try:
            matricula = int(input("Digite a matrícula do aluno: "))
            for aluno in alunos:
                if aluno["matricula"] == matricula:
                    return aluno
        except ValueError:
            print("Matrícula inválida.")
    print("Aluno não encontrado.")
    return None

# ENTREGA DE VERSÕES
def cadastrar_entrega():
    aluno = encontrar_aluno()
    if aluno:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                print("Existe uma entrega pendente de avaliação. Não é possível registrar nova entrega.")
                return
        versao = input("Digite a versão da entrega (ex: v1): ")
        data = input("Digite a data da entrega (YYYY-MM-DD): ")
        entrega = (versao, data, None)
        aluno["entregas"].append(entrega)
        print("Entrega registrada com sucesso.")

# REGISTRO DE NOTAS
def cadastrar_nota():
    aluno = encontrar_aluno()
    if aluno:
        for i, entrega in enumerate(aluno["entregas"]):
            if entrega[2] is None:
                nota = float(input(f"Digite a nota para a versão {entrega[0]} (entregue em {entrega[1]}): "))
                aluno["entregas"][i] = (entrega[0], entrega[1], nota)
                print("Nota registrada com sucesso.")
                return
        print("Não há entregas pendentes para avaliação.")

# LISTAGENS E RELATÓRIOS
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLista de Alunos:")
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Orientador: {aluno['orientador']}")

def listar_alunos_por_orientador():
    for orientador, lista_alunos in orientadores.items():
        print(f"\nOrientador: {orientador}")
        for aluno in lista_alunos:
            print(f"- {aluno}")

def listar_entregas_por_aluno():
    aluno = encontrar_aluno()
    if aluno:
        print(f"\nEntregas do aluno {aluno['nome']}:")
        for entrega in aluno["entregas"]:
            print(f"Versão: {entrega[0]}, Data: {entrega[1]}, Nota: {entrega[2]}")

def listar_pendencias():
    print("\nAlunos com entregas pendentes:")
    for aluno in alunos:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                print(f"- {aluno['nome']} (matrícula: {aluno['matricula']})")
                break

def gerar_relatorio_orientador():
    orientador = input("Digite o nome do orientador: ")
    if orientador not in orientadores:
        print("Orientador não encontrado.")
        return
    total = 0
    count = 0
    print(f"\nRelatório do orientador {orientador}:")
    for nome_aluno in orientadores[orientador]:
        for aluno in alunos:
            if aluno["nome"] == nome_aluno:
                notas = [e[2] for e in aluno["entregas"] if e[2] is not None]
                ultima_nota = notas[-1] if notas else None
                media = sum(notas)/len(notas) if notas else 0
                print(f"- {nome_aluno} | Média: {media:.2f} | Última nota: {ultima_nota}")
                if ultima_nota is not None:
                    total += ultima_nota
                    count += 1
                break
    if count:
        print(f"Média geral (últimas notas): {total / count:.2f}")
    else:
        print("Nenhuma nota registrada ainda.")

# MENUS
def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar orientador")
        print("2 - Cadastrar aluno")
        print("3 - Operações")
        print("q - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_orientador()
        elif opcao == "2":
            cadastrar_aluno()
        elif opcao == "3":
            operacoes()
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def operacoes():
    while True:
        print("\n=== MENU DE OPERAÇÕES ===")
        print("1 - Registrar nova entrega")
        print("2 - Registrar nota")
        print("3 - Listar alunos por orientador")
        print("4 - Listar versões entregues por aluno")
        print("5 - Listar pendências de avaliação")
        print("6 - Gerar relatório do orientador")
        print("7 - Listar todos os alunos cadastrados")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_entrega()
        elif opcao == "2":
            cadastrar_nota()
        elif opcao == "3":
            listar_alunos_por_orientador()
        elif opcao == "4":
            listar_entregas_por_aluno()
        elif opcao == "5":
            listar_pendencias()
        elif opcao == "6":
            gerar_relatorio_orientador()
        elif opcao == "7":
            listar_alunos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

menu()
