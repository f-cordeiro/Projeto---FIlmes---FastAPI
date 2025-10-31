import streamlit as st
import requests

#Criar a URL da API

API_URL = "http://127.0.0.1:8000/"

st.title("Gerenciador de Filmes")

menu = st.sidebar.radio("Menu",
    ["Listar Filmes", "Cadastrar Filmes"]
    )

if menu == "Listar Filmes":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
    else:
        st.error("Erro ao conectar com a API.")
                        