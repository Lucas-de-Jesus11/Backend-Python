'''
Encapsulamento:É um conceito de ocultar detalhes internos de
de um objeto e proteger os dados de acessos externos
'''
#encapsulamento simples
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        #encapsulamento do saldo do titular
        #encapsular o dado usar dois underline
        self.__saldo = saldo #não pode ser chamado
    
    #método depositar
    def depositar(self, valor):
        #ação de depositar um valor ao lado
        self.__saldo += valor
    
    #método de mostrar o saldo ao titular
    def verificar_saldo(self):
        print(f"Olá {self.titular}")
        print(f"Seu saldo é: R${self.__saldo}")

#Criar uma conta e chamar o objeto
conta_maria = ContaBancaria("Maria", 1000)
#exibir o saldo 
conta_maria.verificar_saldo()#saldo de 1000

#depositar valor ao saldo
conta_maria.depositar(500)#deposito de 500
conta_maria.verificar_saldo() #deposito de 1500

#simular o erro de encapsulamento
#chamada do saldo direto
#print(conta_maria.__saldo)#erro