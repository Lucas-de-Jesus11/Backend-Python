'''
Projeto cadastrar aluuno: sistema para calcular 3 notas de 0 a 10
fazer a média das notas, verificar a média do aluno, 
maior ou igual a 6 aprovado, menor que 6 reprovado
salvar e armazenar em uma lista
'''
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
        self.media = self.calcular_media()
        self.situacao = self.definir_situacao()

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def definir_situacao(self):
        return "Aprovado" if self.media >= 6 else "Reprovado"

    def __str__(self):
        return f"Nome: {self.nome}, Notas: {self.notas}, Média: {self.media:.2f}, Situação: {self.situacao}"


class CadastroAlunos:
    def __init__(self):
        self.alunos = []

    def validar_nome(self):
        while True:
            nome = input("Digite o nome e sobrenome do aluno: ").strip()
            if len(nome) >= 5:
                return nome
            else:
                print(f"Nome '{nome}' inválido! O nome precisa ter mais de 5 caracteres.")

    def validar_notas(self):
        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i} (entre 0 e 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Digite um número válido.")
        return notas

    def cadastrar(self):
        while True:
            nome = self.validar_nome()
            notas = self.validar_notas()
            aluno = Aluno(nome, notas)
            self.alunos.append(aluno)

            continuar = input("Digite 's' para sair ou qualquer tecla para continuar: ")
            if continuar.lower() == 's':
                print("Encerrando o cadastro...")
                self.exibir_alunos()
                break

    def exibir_alunos(self):
        print("\nLista de Alunos Cadastrados:")
        for aluno in self.alunos:
            print(aluno)


# Execução do programa
if __name__ == "__main__":
    sistema = CadastroAlunos()
    sistema.cadastrar()