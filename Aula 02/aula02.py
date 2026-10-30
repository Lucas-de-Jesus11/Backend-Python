'''
Recapitulação de função...
mini crud(create, read, update, delete)
sistema do aluno, cadastrar aluno e notas
verificar se está aprovado ou reprovado
'''

#continuação da aula 01 mini crud convertendo para sqlite
import sqlite3

#Sqlite viewer for vs code
#arquivo do banco de dados
BANCO_DE_DADOS = "alunos.db" #nome do arquivo do banco de dados

#1º função que cria o db e inicia e cria a tabela alunos
#colunas: nome, nota1, nota2, media e situação
def conectar_db():
    conexao = sqlite3.connect(BANCO_DE_DADOS)#conecta, se não existir ele cria
    cursor = conexao.cursor()#abrir uma conexão para comandos sql
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   nome TEXT NOT NULL, 
                   nota1 REAL NOT NULL,                     
                   nota2 REAL NOT NULL,                     
                   media REAL NOT NULL,                     
                   situacao TEXT NOT NULL)''')#comandos sql via terminal
#--id auto incremento
#-- TIPO TEXTO NÃO PODE SER NULO
#REAL = float
    #salvar e atualizar o bd
    conexao.commit()
    return conexao, cursor
conectar_db()

#2º função validar nome
def validar_nome():
    while True:#loop de validação
        nome = input("Digite o nome e sobrenome do aluno: ")
        if len(nome) >= 5:
            return nome
        else:
            print("Nome inválido")

#3º função notas
def validar_notas():
    #armazenar em uma lista
    notas = []
    for i in range(1, 3):
        while True:
            try:
                nota = float(input(f"Digite a nota: {i} do aluno entre 0 a 10: "))
                if nota >= 0 and nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Entre 0 a 10")
            except ValueError:
                print("Digite notas númericas entre 0 e 10")
    return notas

#4º função calcular média
def calcular_media(notas):
    media  = sum(notas) / len(notas)
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    return media, situacao

#5º função cadastrar o aluno ao bd
def cadastrar_aluno():
    #while True:#loop de validação do sistema
        #chamar o banco de dados
        conexao, cursor = conectar_db()
        nome = validar_nome()
        notas = validar_notas()
        media, situacao = calcular_media(notas)
        #inserir os comandos sql ao banco de dados alunos.bd
        cursor.execute('''
                    INSERT INTO alunos 
                       (nome, nota1, nota2, media, situacao) 
                    VALUES 
                       (?,?,?,?,?)''',
                    (nome, notas[0],notas[1],media, situacao))
        #atualizar e salvar bd
        conexao.commit()
        #fechar a conexão
        conexao.close()
        #input para mais cadastros
        #continuar = input("Digite 's' para sair ou qualquer tecla para continuar: ").lower()
        #if continuar == "s":
        print("Aluno cadastrado com sucesso...")
        #    print(exibir_alunos())
        #    break
#cadastrar_aluno() - teste

#6º função exibir alunos no terminal
def exibir_alunos():
    #conectar ao banco de dadsos
    conexao, cursor = conectar_db()
    #comandos sql
    cursor.execute("SELECT * FROM alunos")
    #função do python - fethall, leitura de dados
    alunos = cursor.fetchall()#leitura sql
    conexao.close()
    #loop para exibir no terminal ao sair do sistema
    for i in alunos:
        print(f"""
            ID: {i[0]},
            Nome: {i[1]},
            Nota 1: {i[2]},
            Nota 2: {i[3]},
            Média: {i[4]},
            Situação: {i[5]}""")
        print("-"*30)
#cadastrar_aluno()

#7º função para atualizar os dados de um aluno(update)
def atualizar_aluno():
    #exibir alunos para verificar os alunos que irá atualizar
    exibir_alunos()
    #conectar com o bd
    conexao, cursor = conectar_db()
    while True:
        try:
            #editar o aluno pelo ID
            id_aluno = int(input("Digite o ID do aluno para atualizar ou 0 para sair: "))
            if id_aluno == 0:
                print("operação cancelada!")
                break
            #verificar se o aluno existe pelo ID
            cursor.execute(
            "SELECT id FROM alunos WHERE id=?", (id_aluno,))#stop da query
            if cursor.fetchall():#trazer os dados do bd 
            #colocar os dados para atualizar novamente
                nome = validar_nome()
                notas = validar_notas()
                media, situacao = calcular_media(notas)
                #atualizar os dados na tabela
                cursor.execute(
                "UPDATE alunos SET nome =?, nota1=?, nota2=?, media=?, situacao=? WHERE id=?",
                (nome,notas[0],notas[1],media, situacao,id_aluno))
                #salvar a conexao
                conexao.commit()
                print("Aluno atualizado com sucesso!")
                break
            else:
                print("ID inválido, tente novamente.")
        except ValueError:
            print("ERRO, digite um id válio (somente números inteiros)")
    #fecha a conexão
    conexao.close()

#8º função deletar dados do aluno
def deletar_aluno():
    #exibir alunos para verificar os alunos que irá atualizar
    exibir_alunos()
    #conectar com o bd
    conexao, cursor = conectar_db()
    while True:
        try:
            #editar o aluno pelo ID
            id_aluno = int(input("Digite o ID do aluno para deletar ou 0 para sair: "))
            if id_aluno == 0:
                print("operação cancelada!")
                break
            #verificar se o aluno existe pelo ID
            cursor.execute(
            "SELECT id FROM alunos WHERE id=?", (id_aluno,))#stop da query
            if cursor.fetchall():#trazer os dados do bd 
                cursor.execute("DELETE FROM alunos  WHERE id=?",(id_aluno,))
                #salvar a conexao
                conexao.commit()
                print("Aluno deletado com sucesso!")
                break
            else:
                print("ID inválido, tente novamente.")
        except ValueError:
            print("ERRO, digite um id válio (somente números inteiros)")
    #fecha a conexão
    conexao.close()

#menu de escolha
def menu():
    while True:
        print("""
            Menu de escolha
            1- Cadastrar aluno
            2- Exibir todos os alunos
            3- Atualizar aluno
            4- Deletar aluno
            5- Sair """)
        opcao = input("Digite uma opção (1-5): ")
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            exibir_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            deletar_aluno()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente...")
if __name__ == "__main__":
    menu()
#MVC=modelo-visão-controlador
#M=model-lógica da aplicação
#V=view-interface de usuário
#C=controller-intermediário entre o model e view