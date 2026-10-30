'''import mysql.connector

conn = mysql.connector.connect(
            host="127.0.0.1", 
            user="root",
            password="dev1t@24",
            database="db_ecommerce"
)

cur = conn.cursor()
cur.execute("SELECT * FROM produto")
resultados = cur.fetchall()
for linha in resultados:
    print(linha)'''

from sqlalchemy import create_engine, text

class BancoDeDados:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://dev1:dev1t#24@localhost:3306/db_ecommerce')
        self.conn = self.engine.connect()

    def listar_dados(self, tableName):
        query = text(f"SELECT * FROM {tableName}")
        result = self.conn.execute(query)
        return result.fetchall()

    def buscar_dados(self, tableName, coluna, valor):
        query = text(f"SELECT * FROM {tableName} WHERE {coluna} = :valor")
        result = self.conn.execute(query, {"valor": valor})
        return result.fetchall()

    def inserir_dados(self, tableName, colunas, valores):
        qtd_valores = len(valores)
        placeholders = ""

        for i in range(qtd_valores):
            if i < qtd_valores - 1:
                placeholders += f":v{i}, "
            else:
                placeholders += f":v{i}"

        valores_dict = {}
        for i in range(qtd_valores):
            valores_dict[f"v{i}"] = valores[i]

        query = text(f"INSERT INTO {tableName} ({colunas}) VALUES ({placeholders})")
        with self.engine.begin() as conn:
            conn.execute(query, valores_dict)

        print(f"Dados: {valores} \nInseridos na tabela: {tableName}!")

    def deletar_dados(self, tableName, coluna, valor):
        query = text(f"DELETE FROM {tableName} WHERE {coluna} = :valor")
        with self.engine.begin() as conn:
            conn.execute(query, {"valor": valor})

        print(f"{coluna}: {valor} \nRemovido da tabela: {tableName}")

    def fechar_conexao(self):
        self.conn.close()
        self.engine.dispose()

banco = BancoDeDados()
#print(banco.listar_dados("produto"))
#print(banco.buscar_dados("produto", "idProduto", 2))
#banco.inserir_dados("produto", "Nome_Produto, Preço", ["bolsa 1", 10.0])
banco.deletar_dados("produto", "Nome_Produto", "Bolsa Travel Weekender Premium")
# banco.fechar_conexao()