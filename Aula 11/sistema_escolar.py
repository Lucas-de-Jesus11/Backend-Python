'''
Sistema Escolar com POO em Python construção de um sistema
com alunos professores e cursos.
Menu do sistema.
0 - Sair
1 - Ver lista de alunos
2 - Incluir novo aluno
3 - Excluir aluno
4 - Pesquisar aluno
5 - Ver lista de professores
6 - Incluir novo professor
7 - Excluir professor
8 - Pesquisar professor
9 - Ver lista de cursos
10 - Incluir novo curso
11 - Excluir curso
12 - Pesquisar curso
'''
#sistema escolar poo python
class Curso: #representa curso
    def __init__(self, nome, periodo):
        self.nome = nome 
        self.periodo = periodo
    def __str__(self):
        return f"Curso: {self.nome} - Periodo: {self.periodo}"

#class pai para alunos e professores- herança
class Pessoa:
    def __init__(self, nome, data_nasc, matricula):
        self.nome = nome
        self.data_nasc = data_nasc
        self.matricula = matricula

#class filhos professore e aluno
class Professor(Pessoa):
    def __init__(self, nome, disciplina, matricula):
        super().__init__(nome, None, matricula)
        self.disciplina = disciplina
        #professor não precisa passar data de nascimento apenas a disciplina
    #passar uma string nome e disciplina 
    def __str__(self):
        return f"""Professor(a): {self.nome}  
        Disciplina: {self.disciplina}
        Matricula: {self.matricula}"""

class Aluno(Pessoa):
    def __init__(self, nome, documento, matricula):
        #ignoramos data_nasc por simplicidade
        super().__init__(nome, None, matricula)
        self.documento = documento
    def __str__(self):
        return f"""Aluno(a): {self.nome}
                Matricula: {self.matricula}
                Documento: {self.documento}"""

#class principal que gerencia o sistema
class SistemaEscolar:
    def __init__(self):
        #lista para alunos, professores e cursos
        self.alunos = []
        self.professores = []
        self.cursos = []
    #métodos do sistema, listar, incluir, excluir pesquisar
    #método aluno
    def listar_alunos(self):
        #se não tiver aluno cadastrado na lista
        if not self.alunos:
            print("Nenhum aluno cadastrado")
        for i, aluno in enumerate(self.alunos):
            print(f"{i} - {aluno}")
    def incluir_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matricula do aluno: ")
        documento = input("Digite o documento do aluno: ")
        aluno = Aluno(nome, documento, matricula)
        self.alunos.append(aluno)
        print(f"Aluno(a) {nome} adicionado!")
    def excluir_aluno(self):
        self.listar_alunos()
        if self.alunos:
            indice = int(input("Digite o indice a ser excluido: "))
            if 0 <= indice < len(self.alunos):
                alunos_excluido = self.alunos.pop(indice)
                print(f"Aluno excuido {alunos_excluido}")
            else: print("Indice inválido")
    def pesquisar_aluno(self):
        termo = input("Digite o nome do aluno para pesquisar: ").lower()
        encontrados = [
            a for a in self.alunos if termo in a.nome.lower()
        ]
        if encontrados:
            for i in encontrados:
                print(i)
            else:
                print("Aluno não encontrado")
sistema = SistemaEscolar()
sistema.incluir_aluno()
sistema.listar_alunos()
sistema.pesquisar_aluno()
sistema.excluir_aluno()
sistema.incluir_aluno()

'''
exercicio fazer o restante do método professor e curso e menu
'''