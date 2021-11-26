import streamlit as st
import pandas as pd

#####
st.markdown('Dados Financeiros das Ações listadas na bolsa brasileira')

#####
df = pd.read_csv('./Backup/some_file.csv', sep=';', encoding='ISO-8859-1')
view = df[(df['data_dado_inserido'] == '2021-11-25')]
st.dataframe(view)
