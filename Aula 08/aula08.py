#aula 08 POO python

'''
Resolução da atividade 1 e dica para atividade 2.
exercício:POO
criar um sistema em POO para adicionar nome e telefone
de um cliente, e salvar em um arquivo .txt e exibir os
clientes'''

ARQUIVO_CONTATO = "contatos.txt"
class Contato:
    def __init__(self):
        self.clientes = []#atributo lista
    
    def add_cliente(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.clientes.append({"nome": self.nome, "telefone":self.telefone}) #dicionário dentro da lista

#função 
def adicionar_contato():
    #inputs nome e telefone
    nome = input("Nome: ")
    telefone_ = input("Telefone: ")
    #instancia do objeto
    cliente = Contato()
    cliente.add_cliente(nome, telefone_)
    #add em um .txt
    with open(ARQUIVO_CONTATO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}// Telefone: {telefone_}")
    print("Contato salvo")
#função para exibir o contato
def exibir_contato():
    try:
        with open(ARQUIVO_CONTATO, "r", encoding="utf-8") as arquivo:
            for i in arquivo:
                #nome, telefone_ = i.strip()#remover os espaços
                print(f"{i}")
                
    except FileNotFoundError:
        print("Nenhum contato encontrado")

def menu():
    while True:
        print("""
            1 - Adicionar contato:
            2 - Exibir contatos
            3 - Sair""")
        op = input("Escolha: ")
        if op == "1":
            adicionar_contato()
        elif op == "2":
            exibir_contato()
        elif op == "3":
            break
        else:
            print("Opção inválida")
if __name__ == "__main__":
    menu()