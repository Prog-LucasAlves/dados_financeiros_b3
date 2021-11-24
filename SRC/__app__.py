import streamlit as st
import __conectdb__

rows = " SELECT * FROM dados "
result = __conectdb__.se_dados(rows)

st.dataframe(result)
