import streamlit as st
from controllers.usuario_controller import criar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario
#criar a interface para testar o back-end
st.title("Usuários MVC (ORM + python + streamlit)")
#formulário
st.subheader("Adicionar Usuário")
nome=st.text_input("Nome:")
email=st.text_input("Email:")
if st.button("Salvar"):
    criar_usuario(nome,email)
    st.success("Usuário cadastrado")
#listar usuário
st.subheader("Usuários cadastrados")
usuario=listar_usuarios()
for i in usuario:
    st.write(f"ID:{i.id} Nome:{i.nome} Email: {i.email}")

#exercicio simples, refaturar e adicionar o update e delete
st.subheader("Atualizar e deletar usuário")
usuario=listar_usuarios()
if usuario:
    for i in usuario:
        with st.expander(f"{i.nome} {i.email}"):
            novo_nome = st.text_input('Novo nome:', 
                                      value=i.nome, 
                                      key=f"nome:{i.id}")#criar um valor chave para o controller
            novo_email = st.text_input('Novo email:', 
                                       value=i.email, 
                                       key=f"email:{i.id}")
            #colunas
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Atualizar", key=f"Update:{i.id}"):
                    atualizar_usuario(i.id, novo_nome, novo_email)
                    st.success("Usuário atualizado")
                    #recarregar a página
                    st.experimental_rerun()
            with col2:
                if st.button("Deletar", key=f"Deletar:{i.id}"):
                    deletar_usuario(i.id, novo_nome, novo_email)
                    st.success("Usuário deletado")
                    #recarregar a página
                    st.experimental_rerun()