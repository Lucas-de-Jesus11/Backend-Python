'''
exercicio:POO
criar um sistema POO para adicionar nome e telefone de um cliente,
salvar e exibir em um arquivo.txt e exibir os clientes
'''

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone