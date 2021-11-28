import streamlit as st
import pandas as pd

#####
st.subheader('Dados Financeiros das Ações listadas na bolsa brasileira')

#####
# Importando os dados atuais
df = pd.read_csv('./Dados_Atual/dados.csv', sep=';')

# Cria barra lateral
st.sidebar.header("Escolha sua ação")
col1_selection = st.sidebar.selectbox("Papel", df.papel, list(df.papel).index("AALR3"))

# Cria colunas
col1 , col2 = st.columns(2)

#col1.1 - tipo
tipo = df[df['papel'] == col1_selection]
tipo_index = int(tipo['Unnamed: 0'])
tipo_result = tipo['tipo'][tipo_index]
col1.metric(label="Tipo", value = tipo_result)

#col2.1 - empresa
empresa = df[df['papel'] == col1_selection]
empresa_index = int(empresa['Unnamed: 0'])
empresa_result = empresa['empresa'][empresa_index]
col2.metric(label="Empresa", value = empresa_result)

