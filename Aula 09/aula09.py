#aula 09 POO python
'''
Exemplo de código em python com conexão de banco de dados
como objeto, após o exemplo entrega da atividade último dia da entrega.
'''

import sqlite3
#banco de dados de uma loja com produtos
BANCO_DE_DADOS = "loja.db"
class BancoDeDados:
    #construtor do banco de dados para conectar ao banco e executar comandos
    def __init__(self, nome_bd=BANCO_DE_DADOS):
        self.nome_bd = nome_bd
        self.conexao = sqlite3.connect(self.nome_bd)
        self.cursor = self.conexao.cursor()
    
    #método para criar tabela
    def criar_tabela(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS produtos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            preco REAL NOT NULL,
                            quantidade INTEGER NOT NULL)""")
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
    def executar_comando(self, comando, parametros=()):
        self.cursor.execute(comando, parametros)
        self.conexao.commit()
    def buscar_dados(self, comando, parametros=()):
        self.cursor.execute(comando, parametros)
        return self.cursor.fetchall()

#teste
banco = BancoDeDados()
banco.criar_tabela()
banco.executar_comando("""INSERT INTO produtos (
                       nome,preco,quantidade)
                       VALUES (?,?,?)""",
                       ("camisa", 80.90,10))

banco.executar_comando("""INSERT INTO produtos (
                       nome,preco,quantidade)
                       VALUES (?,?,?)""",
                       ("tenis", 306.99,10))
produtos = banco.buscar_dados("SELECT * FROM produtos")
for i in produtos:
    print(f"""
        ID: {i[0]}
        Nome: {i[1]}
        Preço: {i[2]}
        Quantidade: {i[3]}""")
banco.fechar_conexao()