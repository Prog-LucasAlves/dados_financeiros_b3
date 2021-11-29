import streamlit as st
import pandas as pd
import vectorbt as vbt

#####
st.subheader('Dados Financeiros das Ações Listadas na Bolsa Brasileira')

#####
# Importando os dados atuais
df = pd.read_csv('./Dados_Atual/dados.csv', sep=';')

# Cria barra lateral
st.sidebar.header("Escolha sua ação")
col1_selection = st.sidebar.selectbox("Papel", df.papel, list(df.papel).index("ADHM3"))

# Cria colunas
col1 , col2 = st.columns(2)

# col1.1 - tipo
tipo = df[df['papel'] == col1_selection]
tipo_index = int(tipo['Unnamed: 0'])
tipo_result = tipo['tipo'][tipo_index]
col1.metric(label="Tipo", value = tipo_result)

# col2.1 - empresa
empresa = df[df['papel'] == col1_selection]
empresa_index = int(empresa['Unnamed: 0'])
empresa_result = empresa['empresa'][empresa_index]
col2.metric(label="Empresa", value = empresa_result)

st.header('__________')
st.markdown("🚧 - Em contrução")


######
# Backtesting

st.write(
    f" 🚦 Backtesting da Ação {col1_selection} - Cruzamento de Médias Moveis (Rapida -> 17 / Lenta -> 72) \n \
    Intervalo utilizado = Diário / Fechamento"
)
dados_back = vbt.YFData.download_symbol(f"{col1_selection}.SA", start="2000-01-01")
fechamento = dados_back["Close"]
media_rapida = vbt.MA.run(fechamento, 17)
media_lenta = vbt.MA.run(fechamento, 72)
entradas = media_rapida.ma_above(media_lenta, crossover=True)
saidas = media_rapida.ma_below(media_lenta, crossover=True)
pf = vbt.Portfolio.from_signals(fechamento, entradas, saidas)
fig = pf.plot()
st.plotly_chart(fig)
