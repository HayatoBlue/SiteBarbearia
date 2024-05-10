import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='barbas'
)
cursor = conn.cursor()

tab1, tab2 = st.tabs(['+ Barbeiro', '+ Cliente'])

with tab1:
    with st.form('novo-barbeiro', clear_on_submit=True):
        st.header('Cadastrar novo barbeiro')
        novo_barbeiro = st.text_input('Nome: ')
        cadastrar_nv_barbeiro = st.form_submit_button('Cadastrar')
        if cadastrar_nv_barbeiro and novo_barbeiro != "":
            sql = 'INSERT INTO barbeiros (nome) VALUES (%s)'
            dados = (novo_barbeiro,)
            cursor.execute(sql, dados)
            conn.commit()
            st.success(f'Barbeiro {novo_barbeiro} cadastrado', icon="✅")
with tab2:
    with st.form('novo-cliente', clear_on_submit=True):
        st.header('Cadastrar novo cliente')
        nome_cliente = st.text_input('Nome: ')
        cpf_cliente = st.text_input('CPF: ')
        cadastrar_nv_cliente = st.form_submit_button('Cadastrar')
        if cadastrar_nv_cliente and nome_cliente and cpf_cliente != "":
            sql = 'INSERT INTO clientes (nome, cpf) VALUES (%s, %s)'
            dados = (nome_cliente, cpf_cliente,)
            cursor.execute(sql, dados)
            conn.commit()
            st.success(f'Cliente {nome_cliente} cadastrado', icon="✅")
