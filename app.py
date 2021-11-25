import streamlit as st
import pandas as pd

df = pd.read_csv('./Backup/some_file.csv', sep=';')

st.dataframe(df)
