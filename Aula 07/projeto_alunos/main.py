'''
Identificação
Nome: Lucas de Jesus Santos Carvalho
RA: 24271528
Data: 13/08/2025
'''

from banco import CadastroAluno

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