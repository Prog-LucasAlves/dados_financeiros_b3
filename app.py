import streamlit as st
import pandas as pd
import vectorbt as vbt

######
st.subheader('🆚 Informações das Ações Listadas na B3')

######
# Importando os dados atuais
df = pd.read_csv('./Dados_Atual/dados.csv', sep=';')

######
# Cria barra lateral
st.sidebar.header("Escolha sua ação")
col1_selection = st.sidebar.selectbox("Papel", df.papel, list(df.papel).index("AALR3"))

######
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

# col1.2 - data da última cotação
dt_ult_cotacao = df[df['papel'] == col1_selection]
dt_ult_cotacao_index = int(dt_ult_cotacao['Unnamed: 0'])
dt_ult_cotacao_result = dt_ult_cotacao['dt_ult_cotacao'][dt_ult_cotacao_index]
col1.metric(label="Data da Última Cotação", value = dt_ult_cotacao_result )

# col2.2 - valor da cotação
cotacao = df[df['papel'] == col1_selection]
cotacao_index = int(cotacao['Unnamed: 0'])
cotacao_result = cotacao['cotacao'][cotacao_index]
col2.metric(label="Valor da Ação", value = f"R${cotacao_result}")

# col1.3 - máxima do valor da cotação em 52 semanas
max_52_sem = df[df['papel'] == col1_selection]
max_52_sem_index = int(max_52_sem['Unnamed: 0'])
max_52_sem_result = max_52_sem['max_52_sem'][max_52_sem_index]
col1.metric(label="Valor Máximo da Cotação em 52 Semanas", value = f"R${max_52_sem_result}")

# col2.3 - mínima dao valor da cotação em 52 semanas
min_52_sem = df[df['papel'] == col1_selection]
min_52_sem_index = int(max_52_sem['Unnamed: 0'])
min_52_sem_result = min_52_sem['min_52_sem'][min_52_sem_index]
col2.metric(label="Valor Mínimo da Cotação em 52 Semanas", value = f"R${min_52_sem_result}")

######

######
# Backtesting
st.write("-----------------------------------------")
st.write( f" 🚦 Backtesting da Ação {col1_selection}" )
st.write( " 🚦 Estratégia: " ) 
st.write( " 🚦 Cruzamento de Médias Moveis (Rapida -> 17 / Lenta -> 72) " )
st.write( " 🚦 Intervalo utilizado -> Diário(Fechamento) " )

dados_back = vbt.YFData.download_symbol(f"{col1_selection}.SA", start="2000-01-01")
fechamento = dados_back["Close"]
media_rapida = vbt.MA.run(fechamento, 17)
media_lenta = vbt.MA.run(fechamento, 72)
entradas = media_rapida.ma_above(media_lenta, crossover=True)
saidas = media_rapida.ma_below(media_lenta, crossover=True)
pf = vbt.Portfolio.from_signals(fechamento, entradas, saidas)
fig = pf.plot()
st.plotly_chart(fig)

######
# Rodapé
st.write( " ----------------------------------------- " )
st.write( " *Utilize modo light para uma melhor visualização* " )
