import mysql.connector
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
    print(linha)