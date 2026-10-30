'''
Identificação
Nome: Lucas de Jesus Santos Carvalho
RA: 24271528
Data: 13/08/2025
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
    
    def calcular_media(self):
        self.media = sum(self. notas) / len(self.notas)
        self.situacao = "Aprovado" if self.media >= 6 else "Reprovado"