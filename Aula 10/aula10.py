#aula 10 POO python
'''
resolução exercício.
Refatorar o sistema salvar cadastro em 'alunos.db'
no sqlite, dividir o sistema 'modularizar'e fazer seus devidos
importes.
entregue atividade com sua identificação:data, nome e RA.
entregue o print do bando de dados e seus códigos
devidamente modularizado, identificado e comentado
'''
import sqlite3
BANCO_DE_DADOS = "alunos.db"
class BancoDeDados:
    def __init__(self, nome_bd = BANCO_DE_DADOS):
        self.nome_bd = nome_bd
        self.conexao = sqlite3.connect(self.nome_bd)
        self.cursor = self.conexao.cursor()
    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            nota1 REAL NOT NULL,
                            nota2 REAL NOT NULL,
                            media REAL NOT NULL,
                            situacao TEXT NOT NULL)''')
        self.conexao.commit()
    
    def fechar_conexao(self):
        self.conexao.close()
    def executar_comando(self, comando, parametro=()):
        self.cursor.execute(comando, parametro)
        self.conexao.commit()
    def buscar_dados(self, comando):
        self.cursor.execute(comando)
        return self.cursor.fetchall()

class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media, self.situacao = self.calcular_media()
    def calcular_media(self):
        media = (self.nota1+self.nota2+self.nota3) / 3
        situacao = "Aprovado" if media >= 6 else "Reprovado"
        return media, situacao

class GerenciadorAlunos:
    def __init__(self):
        self.bd = BancoDeDados ()
    def validar_notas(self):
        notas = []
        for i in range(1, 4):
            while True:
                try: 
                    nota = float(input(f"Digite a nota {i} 0 a 10: "))
                    if nota >= 0:
                        notas.append(nota)
                        break
                    else:print("Nota invalida")
                except ValueError:
                    print("erro. numero invalido")
        return notas
    def cadastrar_aluno(self):
        nome = input("Nome do aluno: ")
        notas = self.validar_notas()
        aluno = Aluno(nome, notas[0], notas[1], notas[2])
        self.bd.executar_comando('''INSERT INTO alunos(
        nome, nota1, nota2, nota3, media, situacao) VALUES (?,?,?,?,?,?)''',
        (nome, aluno.nota1, aluno.nota2, aluno.nota3, aluno.media, aluno.situacao))
        print("Aluno cadastradi")
    def exibir_alunos(self):
        alunos = self.bd.buscar_dados("SELECT * FROM alunos")
        for i in alunos:
            print(f'''
                    ID: {i[0]}
                    Nome: {i[1]}
                    Nota1: {i[2]}
                    Nota2: {i[3]}
                    Nota3: {i[4]}
                    Media: {i[5]}
                    Situção: {i[6]}''')
            print("")
gerenciar = GerenciadorAlunos()
while True:
    print("""
          1-Cadastrar aluno
          2- Exibir aluno
          3- Sair""")
    op = input("Escolha uma opção: ")
    if op == "1":
        gerenciar.cadastrar_aluno()
    elif op == "2":
        gerenciar.exibir_alunos()
    elif op == "3":
        break
    else:
        print("Opção invalida")
#gerenciar.cadastrar_aluno()