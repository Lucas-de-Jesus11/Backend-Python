#aula16 MVC
'''
Conceito de MVC com o streamlit

estrutura do APP
meu_app//
models/usuario.py #model(ORM)
controllers/usuario_controller.py #Controller python base
app.py #View (streamlit)
database.py #Configuração do banco de dados sqlite

MVC (Model-View-Controller) é um padrão de arquitetura usado
no desenvolvimento de software, incluindo Python, para separar
uma aplicação em três componentes distintos:

Model (Modelo): Este componente manipula os dados e a lógica de
negócios da aplicação. Ele interage com o banco de dados
(ou outras fontes de dados), armazena e recupera dados e
garante a integridade dos dados.
Em frameworks web Python, os modelos são frequentemente
implementados usando Mapeadores Objeto-Relacionais (ORMs)
para representar tabelas de banco de dados como objetos Python.

View (Visualização): Este componente é responsável pela camada
de apresentação, ou seja, o que o usuário vê e com o qual
interage. Ele exibe dados do Modelo e fornece a
interface do usuário. Em aplicações web, isso
normalmente envolve HTML, CSS e JavaScript,
frequentemente renderizados usando mecanismos de modelagem.

Controller (Controlador): Este componente atua como um
intermediário entre o Modelo e a Visão. Ele recebe a
entrada do usuário (por exemplo, solicitações de um
navegador da web), processa a entrada,
interage com o Modelo para executar operações e, em
seguida, atualiza a Visão para refletir as alterações.
'''
