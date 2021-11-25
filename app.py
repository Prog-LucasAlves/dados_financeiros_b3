import streamlit as st
import pandas as pd
from datetime import date

today = date.today()
df = pd.read_csv('./Backup/some_file.csv', sep=';', encoding='ISO-8859-1')


view = df.query(f' data_dado_inserido = {today} ')

st.dataframe(view)
