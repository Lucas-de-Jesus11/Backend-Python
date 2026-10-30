'''
Cadastro produto, nome, preco e quantidade
exibir o produto e quantidade e valor total
'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    #método para saber o valor total do produto
    def valor_produto(self):
        return self.preco * self.quantidade #retornar o valor da mercadoria 
    
    #método para exibir o produto
    def exibir_produto(self):
        print(f"""
            Produto: {self.nome}
            Preço: {self.preco}
            Quantidade: {self.quantidade}
            Valor total: {self.valor_produto()}
            """)
produto1 = Produto("Teclado", 150.00, 10)    
produto2 = Produto("Monitor", 150.00, 10)

#exibir o produto
produto1.exibir_produto()
produto2.exibir_produto()

#input para armazenar os produtos em uma lista
prod = input("Nome do produto: ")
preco = float(input("Preço: "))
quant = float("Quantidade: ")
produtos = Produto(prod, preco, quant)
produtos.exibir_produto()
lista = []
lista.append({"produto":prod, "preco":preco, "quantidade":quant})
print(lista)