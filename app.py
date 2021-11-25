from os import path
import streamlit as st
import __conectdb__

from . import __conectdb__

rows = " SELECT * FROM dados "
result = __conectdb__.se_dados(rows)

st.dataframe(result)
