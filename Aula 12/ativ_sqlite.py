'''
Identificação
Nome: Lucas de Jesus Santos Carvalho
RA: 24271528
Data: 01/09/2025
'''
#mpotando banco de dados
import sqlite3

#Crianco banco de dados
BANCO_DE_DADOS = "SistemaEscolar.db"

#Classe principal do sistena escolar
class SistemaEscolar:
    def __init__(self, nome_bd=BANCO_DE_DADOS):
        self.nome_bd = nome_bd
        self.conexao = sqlite3.connect(self.nome_bd)#conectando ao bd
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        #Tabela de alunos
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL,
            documento TEXT NOT NULL
        )""")
        #Tabela de professores
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL UNIQUE,
            disciplina TEXT NOT NULL
        )""")
        #tabela de cursos
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            periodo TEXT NOT NULL
        )""")

        self.conexao.commit()
    #Funções incluir, listar excluir e pesquisar alunos
    def incluir_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        documento = input("Digite o documento do aluno: ")
        self.cursor.execute(
            "INSERT INTO alunos (nome, matricula, documento) VALUES (?, ?, ?)",
            (nome, matricula, documento)
        )
        self.conexao.commit()
        print(f"Aluno {nome} inserido com sucesso.")

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
        
        id_excluir = int(input("Digite o ID do aluno a ser excluído: "))
        self.cursor.execute("DELETE FROM alunos WHERE id = ?", (id_excluir,))
        self.conexao.commit()
        print("Aluno excluído com sucesso.")
        
    def pesquisar_aluno(self):
        termo = input("Digite o nome do aluno para pesquisar: ").lower()
        self.cursor.execute("SELECT id, nome, matricula, documento FROM alunos WHERE nome = ?", (termo,))
        alunos = self.cursor.fetchall()
        if alunos:
            for a in alunos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Matrícula: {a[2]} | Documento: {a[3]}")
        else:
            print("Aluno não encontrado.")

#------------------PROFESSOR------------
#Funções incluir, listar excluir e pesquisar professores
    def incluir_professor(self):
        nome = input("Digite o nome do professor(a): ")
        matricula = input("Digite a matrícula do professor(a): ")
        disciplina = input("Digite a disciplina do professor(a): ")
        self.cursor.execute(
            "INSERT INTO professores (nome, matricula, disciplina) VALUES (?, ?, ?)",
            (nome, matricula, disciplina)
        )
        self.conexao.commit()
        print(f"Professor(a) {nome} inserido com sucesso.")
    
    def listar_professores(self):
        self.cursor.execute("SELECT id, nome, matricula, disciplina FROM professores")
        professores = self.cursor.fetchall()
        if professores:
            for a in professores:
                print(f"ID: {a[0]} | Nome: {a[1]} | Matrícula: {a[2]} | Disciplina: {a[3]}")
        else:
            print("Nenhum professor cadastrado.")
    
    def excluir_professor(self):
        self.listar_professores()
        id_excluir = int(input("Digite o ID do professor(a) a ser excluído(a): "))
        self.cursor.execute("DELETE FROM professores WHERE id = ?", (id_excluir,))
        self.conexao.commit()
        print("Professor excluído com sucesso.")
    
    def pesquisar_professor(self):
        termo = input("Digite o nome do professor(a) para pesquisar: ").lower()
        self.cursor.execute("SELECT id, nome, matricula, disciplina FROM professores WHERE nome= ?", (termo,))
        professor = self.cursor.fetchall()
        if professor:
            for a in professor:
                print(f"ID: {a[0]} | Nome: {a[1]} | Matrícula: {a[2]} | Disciplina: {a[3]}")
        else:
            print("Professor não encontrado.")
            
#-------------CURSOS-------------------
#Funções incluir, listar excluir e pesquisar cursos
    def incluir_curso(self):
        nome = input("Digite o nome do curso: ")
        periodo = input("Digite o periodo do curso: ")
        self.cursor.execute(
            "INSERT INTO cursos (nome, periodo) VALUES (?, ?)",
            (nome, periodo)
        )
        self.conexao.commit()
        print(f"Curso {nome} adicionado com sucesso.")
    
    def listar_cursos(self):
        self.cursor.execute("SELECT id, nome, periodo FROM cursos")
        cursos = self.cursor.fetchall()
        if cursos:
            for a in cursos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Periodo: {a[2]}")
        else:
            print("Nenhum curso cadastrado.")
    
    def excluir_curso(self):
        self.listar_cursos()
        id_excluir = int(input("Digite o ID do curso a ser excluído(a): "))
        self.cursor.execute("DELETE FROM cursos WHERE id = ?", (id_excluir,))
        self.conexao.commit()
        print("Curso excluído com sucesso.")

    def pesquisar_curso(self):
        termo = input("Digite o nome do curso para pesquisar: ").lower()
        self.cursor.execute("SELECT id, nome, periodo FROM cursos WHERE nome = ?", (termo,))
        cursos = self.cursor.fetchall()
        if cursos:
            for a in cursos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Periodo: {a[2]}")
        else:
            print("Curso não encontrado.")
    
    #função para rodar o sistema
    def executar(self):
        print("Bem vindo ao Sistema Escolar!")
        while True:
            print("""
0 - Sair
1 - Ver lista de alunos
2 - Incluir novo aluno
3 - Excluir aluno
4 - Pesquisar aluno
5 - Ver lista de professores
6 - Incluir novo professor
7 - Excluir professor
8 - Pesquisar professor
9 - Ver lista de cursos
10 - Incluir novo curso
11 - Excluir curso
12 - Pesquisar curso
""")
            opcao = input("Escolha uma opção: ")
            if opcao == "0":
                print("Saindo do sistema...")
                break
            elif opcao == "1": 
                self.listar_alunos()
            elif opcao == "2": 
                self.incluir_aluno()
            elif opcao == "3": 
                self.excluir_aluno()
            elif opcao == "4": 
                self.pesquisar_aluno()

            elif opcao == "5": 
                self.listar_professores()
            elif opcao == "6": 
                self.incluir_professor()
            elif opcao == "7": 
                self.excluir_professor()
            elif opcao == "8": 
                self.pesquisar_professor()

            elif opcao == "9": 
                self.listar_cursos()
            elif opcao == "10": 
                self.incluir_curso()
            elif opcao == "11": 
                self.excluir_curso()
            elif opcao == "12": 
                self.pesquisar_curso()
            else:
                print("Opção inválida. Tente novamente")
if __name__ == "__main__":
     #chamar a classe principal para gerenciar cadastro
    sistema = SistemaEscolar()
    sistema.executar()
