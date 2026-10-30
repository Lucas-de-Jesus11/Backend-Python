'''
Recapitulação de função...
mini crud(create, read, update, delete)
sistema do aluno, cadastrar aluno e notas
verificar se está aprovado ou reprovado
'''
#1º função validar o nome do aluno
def validar_nome():
    while True:
        nome = input("Digite o nome: ")
        if len(nome) >= 5:
            return nome
        else:
            print("Nome invalido")

#2º função validar as notas
def validar_notas():
    notas = []
    for i in range(1, 3):
        while True:
            nota = float(input(
                f"Digite a nota:{i}"))
            if nota <= 0 or nota <=10:
                notas.append(nota)
                break
            else:
                print("Nota inválida")
    return notas

#3º função média
def media(notas):
    media = sum(notas) / len(notas)
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    return media, situacao

#4º função cadastro
def cadastro_alunos(alunos):
    alunos = []
    nome = validar_nome()
    notas = validar_notas()
    media, situacao = media(notas)
    alunos.append({
        "nome":nome, "notas":notas, "media":media,
        "situacao":situacao
    })
#5º função exibir
#6º função editar
#7º função alunos aprovados
#8º menu interativo
#MVC = modelo-visão-controlador
#M=model-lógica da aplicação
#V=view-interface de usuário
#C=controller-intermediário entre o model e view