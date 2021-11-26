import streamlit as st
import pandas as pd
from datetime import date, timedelta

dt = date.today() - timedelta(days=0)
df = pd.read_csv('./Backup/some_file.csv', sep=';', encoding='ISO-8859-1')

st.markdown('Dados Financeiros das Ações listadas na bolsa brasileira')
view = df[(df['data_dado_inserido'] == '2021-11-25')]

st.dataframe(view)
