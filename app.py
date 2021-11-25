import streamlit as st
import sys

import __conectdb__

from . import __conectdb__

sys.path('./SRC/__conectdb__.py')

rows = " SELECT * FROM dados "
result = __conectdb__.se_dados(rows)

st.dataframe(result)
