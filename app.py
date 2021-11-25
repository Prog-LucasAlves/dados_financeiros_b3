import streamlit as st
import pandas as pd

df = pd.read_csv('./Backup/some_file.csv', sep=';', encoding='ISO-8859-1')

st.dataframe(df)
