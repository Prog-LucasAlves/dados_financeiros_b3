import streamlit as st
import pandas as pd

#####
st.markdown('Dados Financeiros das Ações listadas na bolsa brasileira')

#####
df = pd.read_csv('./Dados_Atual/dados.csv', sep=';',)
st.dataframe(df)

# Cria barra lateral
st.sidebar.header("Escolha sua ação")
col1_selection = st.sidebar.selectbox("Papel", df.papel, list(df.papel).index("AALR3"))