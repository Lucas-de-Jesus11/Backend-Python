'''
Identificação
Nome: Lucas de Jesus Santos Carvalho
RA: 24271528
Data: 13/08/2025
'''
import sqlite3
from aluno import Aluno
from config import BANCO_DE_DADOS

class CadastroAluno:
    def __init__(self):
        self.conexao = sqlite3.connect(BANCO_DE_DADOS)#conecta, se não existir ele cria
        self.cursor = self.conexao.cursor()#abrir uma conexão para comandos sql
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL, 
                nota1 REAL NOT NULL,                     
                nota2 REAL NOT NULL,                     
                nota3 REAL NOT NULL,                     
                media REAL NOT NULL,                     
                situacao TEXT NOT NULL)''')
        self.conexao.commit()

    def validar_nome(self):
        #solicitar o nome do aluno
        while True:
            nome = input("Nome do aluno: ")
            return nome
        
    #método cadastro do aluno
    def cadastrar_aluno(self):
        while True:
            nome = self.validar_nome()
            aluno = Aluno(nome)
            aluno.adicionar_notas()
            aluno.calcular_media()
            self.cursor.execute('''
                    INSERT INTO alunos 
                       (nome, nota1, nota2, nota3, media, situacao) 
                    VALUES 
                       (?,?,?,?,?,?)''',
                    (aluno.nome, aluno.notas[0],aluno.notas[1],aluno.notas[2],aluno.media, aluno.situacao))
            #atualizar e salvar bd
            self.conexao.commit()
            continuar = input("'s' para sair ou continuar cadastrando...").lower()
            if continuar == "s":
                print("Cadastro finalizado")
                break
    def exibir_alunos(self):
        #comandos sql
        self.cursor.execute("SELECT * FROM alunos")
        #função do python - fethall, leitura de dados
        alunos = self.cursor.fetchall()#leitura sql
        self.conexao.close()
        #loop para exibir no terminal ao sair do sistema
        for i in alunos:
            print(f"""
                ID: {i[0]},
                Nome: {i[1]},
                Nota 1: {i[2]},
                Nota 2: {i[3]},
                Nota 3: {i[4]},
                Média: {i[5]},
                Situação: {i[6]}""")
            print("-"*30)
