#aula12 
#POO python
'''
Descrição da atividade:
Esta atividade tem como objetivo transformar os dados salvos
em memória (listas) em registros armazenados em
um banco de dados.
Inicialmente, o SQLite para realização de testes completos e
validação do processo. Após a conclusão dos testes,
a aplicação será migrada para o MariaDB, rodando em um servidor
de banco de dados em produção.
Como parte da entrega, será necessário apresentar:
-Um print do código implementado com SQLite;
-Um print do código adaptado para MariaDB;
-Os códigos referentes aos cadastros realizados no servidor
MariaDB.
'''

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
    
    def listar_professores(self):
        if not self.professores:
            print("Nenhum professor cadastrado")
        for i, prof in enumerate(self.professores):
            print(f"{i} - {prof}")
    
    def incluir_professor(self):
        nome = input("Digite o nome do professor: ")
        disciplina = input("Digite a disciplina: ")
        matricula = input("Digite a matricula: ")
        professor = Professor(nome, disciplina, matricula)
        self.professores.append(professor)
        print(f"Professor {nome} incluido com sucesso!")
    
    def excluir_professor(self):
        self.listar_professores()
        if self.professores:
            indice = int(input("Digite o indice do professor a ser excluido: "))
            if 0 <= indice < len(self.professores):
                prof_excluido = self.professores.pop(indice)
                print(f"Professor {prof_excluido.nome} excluido")
            else:
                print("Indice invalido")
    
    def pesquisar_professor(self):
        termo = input("Digite o nome do professor para pesquisar: ").upper()
        encontrados = [p for p in self.professores if termo in p.nome.upper()]
        if encontrados:
            for prof in encontrados:
                print(prof)
        else:
            print("Professor não encontrado")
    
    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
        for i, curso in enumerate(self.cursos):
            print(f"{i} - {curso}")
    
    def incluir_curso(self):
        nome = input("Digite o nome do curso: ")
        periodo = input("Digite o periodo do curso: ")
        curso = Curso(nome, periodo)
        self.cursos.append(curso)
        print(f"Curso {nome} incluido com sucesso!")
    
    def excluir_curso(self):
        self.listar_cursos()
        if self.cursos:
            indice = int(input("Digite o indice do curso a ser excluido: "))
            if 0 <= indice < len(self.cursos):
                curso_excluido = self.cursos.pop(indice)
                print(f"Curso {curso_excluido.nome} excluido")
            else:
                print("Indice invalido")

    def pesquisar_curso(self):
        termo = input("Digite o nome do curso para pesquisa: ").upper()
        encontrados = [c for c in self.cursos if termo in c.nome.upper()]
        if encontrados:
            for curso in encontrados:
                print(curso)
        else:
            print("Curso não encontrado")
    
    def executar(self):
        print("Bem vindo ao Sistema Escolar!")
        while True:
            print("""
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
""")
            opcao = input("Escolha uma opção: ")
            if opcao == "0":
                print("Saindo do sistema...")
                break
            elif opcao == "1": self.listar_alunos()
            elif opcao == "2": self.incluir_aluno()
            elif opcao == "3": self.excluir_aluno()
            elif opcao == "4": self.pesquisar_aluno()

            elif opcao == "5": self.listar_professores()
            elif opcao == "6": self.incluir_professor()
            elif opcao == "7": self.excluir_professor()
            elif opcao == "8": self.pesquisar_professor()

            elif opcao == "9": self.listar_cursos()
            elif opcao == "10": self.incluir_curso()
            elif opcao == "11": self.excluir_curso()
            elif opcao == "12": self.pesquisar_curso()
            else:
                print("Opção inválida. Tente novamente")
if __name__ == "__main__":
    sistema = SistemaEscolar()
    sistema.executar()