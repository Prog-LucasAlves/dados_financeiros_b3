import streamlit as st
import pandas as pd
from streamlit.state.session_state import Value

#####
st.subheader('Dados Financeiros das Ações listadas na bolsa brasileira')

#####
df = pd.read_csv('./Dados_Atual/dados.csv', sep=';')

# Cria barra lateral
st.sidebar.header("Escolha sua ação")
col1_selection = st.sidebar.selectbox("Papel", df.papel, list(df.papel).index("AALR3"))

# Cria colunas
col1 , col2 = st.columns(2)

#col1 - papel
papel = df[df['papel'] == col1_selection]
papel_index = int(papel['Unnamed: 0'])
papel_result = papel['papel'][papel_index]
col1.metrics(labe="Papel", value=papel_result)


    