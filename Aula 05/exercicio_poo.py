'''
Identificação
Nome: Lucas de Jesus Santos Carvalho
RA: 24271528
Matéria: BACK-END pt.2
Data: 06/08/2025
'''
#aula05 Atividade....
'''
exercício:POO
criar um sistema em POO para adicionar nome e telefone
de um cliente, e salvar em um arquivo .txt e exibir os
clientes
entregar o print do seu código e identificação
'''

class Usuario:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}"
    
class GerenciarUsuarios:
    def __init__(self, arquivo="usuarios.txt"):
        self.usuarios = []
        self.arquivo = arquivo
        self.carregar_dados()
    
    #Função carregar dados do arquivo ao iniciar o programa
    def carregar_dados(self):
        try:#erro ao carregar o arquivo se não existir
            with open(self.arquivo, "r") as arquivo:
                #loop carregar linha por linha para cada dado
                for linha in arquivo:#dividir a linha em um nome, telefone e email
                    dados = linha.strip().split(", ")#retira o espaço do txt e separa por ,
                    #extrair os valores após as chaves do dicionário
                    #replace= cria uma cópia do arquivo original sem modificar
                    nome = dados[0].replace("Nome: ", "")
                    telefone = dados[1].replace("Telefone: ", "")
                    self.usuarios.append(Usuario(nome, telefone))
        except FileNotFoundError:
            #se o arquivo não exite "usuarios.txt" começa com uma lista vazia
            #para não parar o programa
            pass
    
    def adicionar_usuario(self, nome, telefone):
        self.usuarios.append(Usuario(nome, telefone))
        print(f"\nUsuário {nome} adicionado com sucesso!")
    
    def visualizar_usuarios(self):
        if not self.usuarios:
            print("\nNenhum usuário cadastrado")
        else:
            print("\nUsuários cadastrados:")
            for usuario in self.usuarios:
                print(usuario)
    
    def salvar_arquivo(self):
        with open(self.arquivo, "w") as arquivo:
            for usuario in self.usuarios:
                arquivo.write(str(usuario) +"\n")
        print(f"\nUsuários salvos no arquivo {self.arquivo}")
    
def menu():
    gerenciador = GerenciarUsuarios()
    while True:
        opcao = input("""
                Menu:
                1 - Adicionar usuário
                2 - Visualizar usuários
                3 - Sair e salvar
                Escolha uma opção: """)
        if opcao == "1":
            nome = input("Digite seu nome: ")
            telefone = input("Digite o telefone: ")
            gerenciador.adicionar_usuario(nome, telefone)
        
        elif opcao == "2":
            gerenciador.visualizar_usuarios()
        
        elif opcao == "3":
            gerenciador.salvar_arquivo()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente")
menu()