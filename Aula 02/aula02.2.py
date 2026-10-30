'''
Recapitulação de função...
mini crud(create, read, update, delete)
sistema do aluno, cadastrar aluno e notas
verificar se está aprovado ou reprovado
'''
import sqlite3
#ORM = objeto para conectar e criar o banco
#1°função validar o nome do aluno
"""def validar_nome():
    while True:
        nome=input("Digite o nome.")
        if len(nome)>=5:
            return nome
        else:
            print("Nome inválido.")
#2°função validar as notas
def validar_notas():
    notas=[]
    for i in range(1,3):
        while True:
            nota=float(input(
        f"Digite a nota:{i}"))
            if nota <=0 or nota <=10:
                notas.append(nota)
                break
            else:print("Nota inválida")
    return notas
#3°função média
def calcular_media(notas):
    media=sum(notas)/len(notas)
    situacao="aprovado" if media >=6 else "Reprovado"
    return media,situacao
#4°função cadastro
def cadastro_alunos():
    alunos=[]
    nome=validar_nome()
    notas=validar_notas()
    media,situacao=calcular_media(notas)
    alunos.append({
        "nome":nome,"notas":notas,"media":media,
        "situacao":situacao
    })
cadastro_alunos()"""
#5°função exibir
#6°função editar
#7°função alunos aprovados e reprovados
#8°menu interativo
#MVC=modelo-visão-controlador
#M=model-lógica da aplicação
#V=view-interface de usuário
#C=controller-intermediário entre o model e view

#crud alunos
#import sqlite3
#conctar criar banco de dados
#ORM=objto para conectar e criar o banco
import sqlite3
#1°função validar o nome do aluno
"""def validar_nome():
    while True:
        nome=input("Digite o nome.")
        if len(nome)>=5:
            return nome
        else:
            print("Nome inválido.")
#2°função validar as notas
def validar_notas():
    notas=[]
    for i in range(1,3):
        while True:
            nota=float(input(
        f"Digite a nota{i}: "))
            if nota <=0 or nota <=10:
                notas.append(nota)
                break
            else:print("Nota inválida")
    return notas
#3°função média
def calcular_media(notas):
    media=sum(notas)/len(notas)
    situacao="aprovado" if media >=6 else "Reprovado"
    return media,situacao
#4°função cadastro
def cadastro_alunos():
    alunos=[]
    nome=validar_nome()
    notas=validar_notas()
    media,situacao=calcular_media(notas)
    alunos.append({
        "nome":nome,"notas":notas,"media":media,
        "situacao":situacao
    })
cadastro_alunos()"""
#5°função exibir
#6°função editar
#7°função alunos aprovados e reprovados
#8°menu interativo
#MVC=modelo-visão-controlador
#M=model-lógica da aplicação
#V=view-interface de usuário
#C=controller-intermediário entre o model e view


#conctar criar banco de dados
#ORM=objto para conectar e criar o banco
conectar=sqlite3.connect("alunos.db")
cursor=conectar.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nota1 REAL NOT NULL,
               nota2 REAL NOT NULL,
               media REAL NOT NULL,
               situacao TEXT NOT NULL)''')
conectar.commit()

#1°função validar o nome do aluno
def validar_nome():
    while True:
        nome=input("Digite o nome.")
        if len(nome)>=5:
            return nome
        else:
            print("Nome inválido.")
#2°função validar as notas
def validar_notas():
    notas=[]
    for i in range(1,3):
        while True:
            nota=float(input(
        f"Digite a nota{i}: "))
            if nota <=0 or nota <=10:
                notas.append(nota)
                break
            else:print("Nota inválida")
    return notas
#3°função média
def calcular_media(notas):
    media=sum(notas)/len(notas)
    situacao="aprovado" if media >=6 else "Reprovado"
    return media,situacao
#4°função cadastro
def cadastro_alunos():
    #alunos=[]
    #while True:
        nome=validar_nome()
        notas=validar_notas()
        media,situacao=calcular_media(notas)
        cursor.execute(
        '''INSERT INTO alunos (
        nome,nota1,nota2,media,situacao) VALUES (?,?,?,?,?)''',
        (nome,notas[0],notas[1],media,situacao))
        '''
        continuar=input(
            "'s' para sair ou cintinue cadastrando").lower()
        if continuar=="s":
            break
        '''
        conectar.commit()
    #conectar.close()
#cadastro_alunos()
def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    for i in cursor.fetchall():
        print(i)
def atualizar_aluno():
    listar_alunos()
    aluno_id=input("ID do aluno para atualizar. ")
    nome=validar_nome()
    notas=validar_notas()
    media,situacao=calcular_media(notas)
    cursor.execute("""UPDATE alunos SET nome=?,
        nota1=?,nota2=?,media=?,situacao=? WHERE id=?""",
        (nome,notas[0],notas[1],media,situacao,aluno_id))
    conectar.commit()
    print("Aluno atualizado!")
#atualizar_aluno()
def deletar_aluno():
    listar_alunos()
    aluno_id=input("ID do aluno para deletar. ")
    cursor.execute("DELETE FROM alunos WHERE id=?",
                   (aluno_id,))
    conectar.commit()
    print("Aluno deletado!")
#deletar_aluno()
def menu():
    while True:
        print("""MENU CRUD alunos.
          1 - cadastrar.
          2 - listar.
          3 - atualizar.
          4 - deltar.
          5 - sair.""")
        op=input("Escolha uma opção: ")
        if op =="1":
         cadastro_alunos()
        elif op =="2":
            listar_alunos()
        elif op =="3":
            atualizar_aluno()
        elif op =="4":
            deletar_aluno()
        elif op =="5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção errada.")
if __name__=="__main__":
    menu()
conectar.close()
#MVC = modelo-visão-controlador
#M=model-lógica da aplicação
#V=view-interface de usuário
#C=controller-intermediário entre o model e view