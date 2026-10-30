#aula 07 POO python
'''
exercício para treinamento: converter o castro aluno em POO

Projeto: Cadastro de alunos e cáculo de médias,
cadastrar o aluno colocar as notas, fazer as médias
e verificar a situação do aluno
cadastrar nome:
cadastrar 3 notas:
fazer a média:
situação: >=6 aprovado <6 reprovado
'''

#class representa um aluno com nome, notas, média e situação
class Aluno:
    def __init__(self, nome):
        self.nome = nome #nome do aluno
        self.notas = notas = [] #armazenar  notas em uma lista do aluno
        self.media = 0.0 #média vazia para mudar assim que passar a média
        self.situacao = "" #str vazio para adicionar ao saebr a média
    
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
    
    #método para média e situação
    def calcular_media(self):
        self.media = sum(self. notas) / len(self.notas)
        self.situacao = "Aprovado" if self.media >= 6 else "Reprovado"
    
    #método para exibir resultados
    def exibir_dados(self):
        print(f"""
            Nome: {self.nome}
            Notas: {self.notas}
            Média: {self.media}
            Situação: {self.situacao}""")

#class gerencia o cadastro de alunos
class CadastroAluno:
    #inicializar a classe com __init__
    def __init__(self):
        self.alunos_ = [] #lista de alunos
     #método validar o nome, cadastrar e exibir
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
            #armazenar na lista
            self.alunos_.append(aluno)
            continuar = input("'s' para sair ou continuar cadastrando...").lower()
            if continuar == "s":
                print("Cadastro finalizado")
                break
    #método exibir todos os alunos
    def exibir_alunos(self):
        for i in self.alunos_:
            i.exibir_dados()#pega da class alunos

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