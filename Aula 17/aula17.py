#aula18 rotas api com templetes padrão mvc

#arquitetura do projeto rota controller com view
'''
-projeto_mvc/
main.py #ponto de entrada da aplicação
database.py #conexão com o banco de dados Sqlite
models.py #modelos ORM Sqlalchemy
controller.py #regras de negócio e rotas
-view/ #templetes Jinja2
--  index.html#front html
'''
#-ordem projeto_mvc
#1-Definir conexão com Sqlite - database.py
#2-Definir modelo ORM -models.py
#3-Regras de negócio e rotas controller.py
#4-templete inicial -index.html
#5-ponto de entrada da aplicação - main.py