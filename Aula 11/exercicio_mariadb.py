'''
exercicio simples converter a atividade 2 sqlite para o maria db
'''
import mysql.connector

BANCO_DE_DADOS = {
    'host':'localhost', #local do servidor de banco de dados 
    'user': 'root',#usuário que vai logar no servidor
    'password': 'dev1t@24', #senha para logar no servidor
    'database': 'lucas' #nome do banco de dados 
}

#class representa um aluno com nome, notas, média e situação
class Aluno:
    def __init__(self, nome):
        self.nome = nome #nome do aluno
        self.notas = notas = [] #armazenar  notas em uma lista do aluno
        self.media = 0.0 #média vazia para mudar assim que passar a média
        self.situacao = "" #str vazio para adicionar ao saber a média
    
    #métodos adiconar notas, calcular média e situação
    def adicionar_notas(self):
        #solicitar as tres notas
        for i in range(1, 4):#3 notas
            while True:
                try:
                    nota = float(input(f"Digite a nota {i} entre 0 e 10: "))
                    if nota >= 0:
                        if nota <= 10:
                            self.notas.append(nota)
                            break
                    else:
                        print("Erro nota entre 0 a 10")
                except ValueError:
                    print("Erro, digite uma nota válida")
    
    def calcular_media(self):
        self.media = sum(self. notas) / len(self.notas)
        self.situacao = "Aprovado" if self.media >= 6 else "Reprovado"

class CadastroAluno:
    def __init__(self):
        self.conexao = mysql.connector.connect(**BANCO_DE_DADOS)#conecta, se não existir ele cria
        self.cursor = self.conexao.cursor()#abrir uma conexão para comandos sql
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                nome VARCHAR(100) NOT NULL, 
                nota1 FLOAT NOT NULL,                     
                nota2 FLOAT NOT NULL,
                nota3 FLOAT NOT NULL,                     
                media FLOAT NOT NULL,                     
                situacao VARCHAR(20) NOT NULL)''')
        self.conexao.commit()
#CadastroAluno()
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
                       (%s, %s, %s, %s, %s, %s)''',
                    (aluno.nome, aluno.notas[0],aluno.notas[1],aluno.notas[2], aluno.media, aluno.situacao))
            #atualizar e salvar bd
            self.conexao.commit()
            continuar = input("'s' para sair ou continuar cadastrando...").lower()
            if continuar == "s":
                print("Cadastro finalizado")
                break
    def exibir_alunos(self):
        #conectar ao banco de dadsos
        #self.conexao, self.cursor = conectar_db()
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

#função main para rodar o programa
def main():
    print("Cadastro de alunos...")
    #chamar a classe principal para gerenciar cadastro
    sistema = CadastroAluno()
    #chamar o método para cadastrar aluno
    sistema.cadastrar_aluno()
    #chamar método para exibir alunos
    sistema.exibir_alunos()
if __name__ == "__main__":
    main()