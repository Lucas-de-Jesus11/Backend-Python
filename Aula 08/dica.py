#dica do banco de dados - sistema criar tarefas
import sqlite3
BANCO_DE_DADOS = "tarefas.db"
class Tarefa:
    def __init__(self, descricao, status="pendente"):
        self.descricao = descricao
        self.status = status
    
class BancoDeDados:
    def __init__(self, nome_bd=BANCO_DE_DADOS):#método construtor para criar
        self.nome_bd = nome_bd#inicia o bd tarefas.db
        self.conexao = sqlite3.connect(self.nome_bd)#conectar ao bd
        self.cursor = self.conexao.cursor()#executa comandos sql
        self.criar_tabela()
    
    def criar_tabela(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS tarefas(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            descricao TEXT NOT NULL,
                            status TEXT NOT NULL)''')
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
    def executar_comandos(self, comando, parametro=()):
        self.cursor.execute(comando, parametro)
        self.conexao.commit()
    def buscar_dados(self, comando):
        self.cursor.execute(comando)
        return self.cursor.fetchall()

tarefa1 = input("Digite a tarefa: ")
descricao = input("Descrição: ")
#instancia do banco de dados 
tarefa = Tarefa(tarefa1, descricao)
banco = BancoDeDados()
banco.executar_comandos("""INSERT INTO tarefas (
                        descricao, status)
                        VALUES (?,?)""", 
                        (tarefa1, descricao))
exibir = banco.buscar_dados("SELECT * FROM tarefas")
for i in exibir:
    print(f"tarefa: {i[1]} - status: {i[2]}")