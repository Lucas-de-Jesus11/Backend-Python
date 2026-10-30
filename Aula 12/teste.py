import sqlite3

BANCO_DE_DADOS = "SistemaEscolar.db"

class SistemaEscolarDB:
    def __init__(self, nome_bd=BANCO_DE_DADOS):
        self.nome_bd = nome_bd
        self.conexao = sqlite3.connect(self.nome_bd)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL UNIQUE,
            documento TEXT NOT NULL
        )""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL UNIQUE,
            disciplina TEXT NOT NULL
        )""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            periodo TEXT NOT NULL
        )""")

        self.conexao.commit()

    def incluir_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        documento = input("Digite o documento do aluno: ")

        try:
            self.cursor.execute(
                "INSERT INTO alunos (nome, matricula, documento) VALUES (?, ?, ?)",
                (nome, matricula, documento)
            )
            self.conexao.commit()
            print(f"Aluno {nome} inserido com sucesso.")
        except sqlite3.IntegrityError:
            print("Erro: matrícula já cadastrada.")

    def listar_alunos(self):
        self.cursor.execute("SELECT id, nome, matricula, documento FROM alunos")
        alunos = self.cursor.fetchall()
        if alunos:
            for a in alunos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Matrícula: {a[2]} | Documento: {a[3]}")
        else:
            print("Nenhum aluno cadastrado.")

    def excluir_aluno(self):
        self.listar_alunos()
        try:
            id_excluir = int(input("Digite o ID do aluno a ser excluído: "))
            self.cursor.execute("DELETE FROM alunos WHERE id = ?", (id_excluir,))
            self.conexao.commit()
            print("Aluno excluído com sucesso.")
        except ValueError:
            print("ID inválido.")
        except Exception as e:
            print("Erro ao excluir aluno:", e)

    def pesquisar_aluno(self):
        termo = input("Digite o nome do aluno para pesquisar: ").lower()
        self.cursor.execute("SELECT id, nome, matricula, documento FROM alunos WHERE LOWER(nome) LIKE ?", (f"%{termo}%",))
        alunos = self.cursor.fetchall()
        if alunos:
            for a in alunos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Matrícula: {a[2]} | Documento: {a[3]}")
        else:
            print("Aluno não encontrado.")

    def fechar_conexao(self):
        self.conexao.close()
if __name__ == "__main__":
    sistema = SistemaEscolarDB()

    while True:
        print("""
1 - Incluir aluno
2 - Listar alunos
3 - Excluir aluno
4 - Pesquisar aluno
0 - Sair
""")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            sistema.incluir_aluno()
        elif opcao == "2":
            sistema.listar_alunos()
        elif opcao == "3":
            sistema.excluir_aluno()
        elif opcao == "4":
            sistema.pesquisar_aluno()
        elif opcao == "0":
            sistema.fechar_conexao()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")
