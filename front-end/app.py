import streamlit as st
import requests

#Criar a URL da API

API_URL = "http://127.0.0.1:8000/"

st.set_page_config(page_title="Filmes", layout="wide")
st.title("Gerenciador de Filmes")

menu = st.sidebar.radio("Menu",
    ["Listar Filmes", "Cadastrar Filmes", "Deletar Filmes", "Atualizar Filmes"]
    )

if menu == "Listar Filmes":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            st.dataframe(filmes)
        else:
            st.info("Nenhum filme cadastrado ainda!")
    else:
        st.error("Erro ao conectar com a API.")

elif menu == "Cadastrar Filmes":
    st.subheader("➕ Cadastrar Filmes")
    titulo = st.text_input("Título do Filme")
    genero = st.text_input("Gênero do Filme")
    ano = st.number_input("Ano de lançamento", min_value=1878, max_value=2100, step=1)
    nota = st.number_input("Nota (0 á 10)", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Salvar filme"):
        dados = { "titulo": titulo, "genero": genero, "ano": ano, "nota": nota}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar filme.")

elif menu == "Deletar Filmes":
    st.subheader("🗑 Deletar Filmes")
    id_filme = st.number_input("Id do filme a excluir", min_value=1, step=1) 
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/filmes/{id_filme}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Filme excluído com sucesso!")
            else:
                st.error("Erro ao tentar excluir filme")

elif menu == "Atualizar Filmes":
    st.subheader("Atualizar Filmes")
    id_filme = st.number_input("Id do filme para atualizar", min_value=1, step=1)
    nova_nota = st.number_input("Nota (0 á 10)", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Atualizar"):
        dados = {
            "id_filme": id_filme,
            "nova_nota": nova_nota
        }
        response = requests.put(f"{API_URL}/filmes/{id_filme}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Nota do Filme atualizada com sucesso!")
            else:
                st.warning(data["erro"])
        else:
            st.error("Erro ao atualizar filme.")