import streamlit as st
import pandas as pd
import vectorbt as vbt
import re
from datetime import datetime

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
col1.metric(label="Tipo", value=tipo_result)

# col2.1 - empresa
empresa = df[df['papel'] == col1_selection]
empresa_index = int(empresa['Unnamed: 0'])
empresa_result = empresa['empresa'][empresa_index]
col2.metric(label="Empresa", value=empresa_result)

# col1.2 - data da última cotação
dt_ult_cotacao = df[df['papel'] == col1_selection]
dt_ult_cotacao_index = int(dt_ult_cotacao['Unnamed: 0'])
dt_ult_cotacao_result = dt_ult_cotacao['dt_ult_cotacao'][dt_ult_cotacao_index]
col1.metric(label="Data da Última Cotação", value=dt_ult_cotacao_result, delta="Janeiro")

# col2.2 - valor da cotação + Variação do dia anterior
cotacao = df[df['papel'] == col1_selection]
cotacao_index = int(cotacao['Unnamed: 0'])
cotacao_result = cotacao['cotacao'][cotacao_index]

os_dia = df[df['papel'] == col1_selection]
os_dia_index = int(os_dia['Unnamed: 0'])
os_dia_result = os_dia['os_dia'][os_dia_index]

col2.metric(label="Valor da Ação", value=f"R${cotacao_result}", delta=f"{os_dia_result}%")

# col1.3 - máxima do valor da cotação em 52 semanas
max_52_sem = df[df['papel'] == col1_selection]
max_52_sem_index = int(max_52_sem['Unnamed: 0'])
max_52_sem_result = max_52_sem['max_52_sem'][max_52_sem_index]
col1.metric(label="Valor Máximo da Ação em 52 Semanas", value=f"R${max_52_sem_result}")

# col2.3 - mínima dao valor da cotação em 52 semanas
min_52_sem = df[df['papel'] == col1_selection]
min_52_sem_index = int(max_52_sem['Unnamed: 0'])
min_52_sem_result = min_52_sem['min_52_sem'][min_52_sem_index]
col2.metric(label="Valor Mínimo da Ação em 52 Semanas", value=f"R${min_52_sem_result}")

# col1.4 - volume de negociações
vol_med = df[df['papel'] == col1_selection]
vol_med_index = int(vol_med['Unnamed: 0'])
vol_med_result = vol_med['vol_med'][vol_med_index]
col1.metric(label="Volume médio de Negociações(2 meses)", value=f"R${vol_med_result},00")

# col2.4 - valor de mercado da empresa
valor_mercado = df[df['papel'] == col1_selection]
valor_mercado_index = int(valor_mercado['Unnamed: 0'])
valor_mercado_result = valor_mercado['valor_mercado'][valor_mercado_index]
col2.metric(label="Valor de Mercado", value=f"R${valor_mercado_result},00")

# col1.5 - valor da firma
valor_firma = df[df['papel'] == col1_selection]
valor_firma_index = int(valor_firma['Unnamed: 0'])
valor_firma_result = valor_firma['valor_firma'][valor_firma_index]
col1.metric(label="Valor da Firma", value=f"R${valor_firma_result},00")

# col2.5 - número de ações em circulação
nr_acoes = df[df['papel'] == col1_selection]
nr_acoes_index = int(nr_acoes['Unnamed: 0'])
nr_acoes_result = nr_acoes['nr_acoes'][nr_acoes_index]
nr_acoes_int = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(nr_acoes_result))
col2.metric(label="Número de Ações em Circulação", value=nr_acoes_int)

# col1.6 - preço / lucro
pl = df[df['papel'] == col1_selection]
pl_index = int(pl['Unnamed: 0'])
pl_result = pl['pl'][pl_index]
col1.metric(label="P/L - (Preço/Lucro)", value=f"{pl_result:.2f}")

# col2.6 - lucro por ação
lpa = df[df['papel'] == col1_selection]
lpa_index = int(lpa['Unnamed: 0'])
lpa_result = lpa['lpa'][lpa_index]
col2.metric(label="LPA - (Lucro por Ação)", value=f"{lpa_result:.2f}")

# col1.7 - preço / valor patrimonial por ação
pvp = df[df['papel'] == col1_selection]
pvp_index = int(pvp['Unnamed: 0'])
pvp_result = pvp['pvp'][pvp_index]
col1.metric(label="P/VP - (Preço/Valor Patrimonial por Ação)", value=f"{pvp_result:.2f}")

# col2.7 - valor patrimonial por ação
vpa = df[df['papel'] == col1_selection]
vpa_index = int(vpa['Unnamed: 0'])
vpa_result = vpa['vpa'][vpa_index]
col2.metric(label="VPA - (Valor Patrimonial por Ação)", value=f"{vpa_result:.2f}")

# col1.8 - preço da ação divido pelo ebit por ação
p_ebit = df[df['papel'] == col1_selection]
p_ebit_index = int(p_ebit['Unnamed: 0'])
p_ebit_result = p_ebit['p_ebit'][p_ebit_index]
col1.metric(label="P/EBIT - (Preço/Ebit por Ação)", value=f"{p_ebit_result:.2f}")

# col2.8 - margem bruta
marg_bruta = df[df['papel'] == col1_selection]
marg_bruta_index = int(marg_bruta['Unnamed: 0'])
marg_bruta_result = marg_bruta['marg_bruta'][marg_bruta_index]
col2.metric(label="Margem Bruta", value=f"{marg_bruta_result:.2f}%")

# col1.9 - psr
psr = df[df['papel'] == col1_selection]
psr_index = int(psr['Unnamed: 0'])
psr_result = psr['psr'][psr_index]
col1.metric(label="PSR", value=f"{psr_result:.2f}")

# col2.9 - margem ebit
marg_ebit = df[df['papel'] == col1_selection]
marg_ebit_index = int(marg_ebit['Unnamed: 0'])
marg_ebit_result = marg_ebit['marg_ebit'][marg_ebit_index]
col2.metric(label="Margem Ebit", value=f"{marg_ebit_result:.2f}%")

# col1.10 - P/Ativo
p_ativo = df[df['papel'] == col1_selection]
p_ativo_index = int(p_ativo['Unnamed: 0'])
p_ativo_result = p_ativo['p_ativo'][p_ativo_index]
col1.metric(label="P/Ativos", value=f"{p_ativo_result:.2f}")

# col2.10 - margem liquida
marg_liquida = df[df['papel'] == col1_selection]
marg_liquida_index = int(marg_liquida['Unnamed: 0'])
marg_liquida_result = marg_liquida['marg_liquida'][marg_liquida_index]
col2.metric(label="Margem Líquida", value=f"{marg_liquida_result:.2f}%")

# col1.11 - preço dividido pelo capital de giro por ação
p_cap_giro = df[df['papel'] == col1_selection]
p_cap_giro_index = int(p_cap_giro['Unnamed: 0'])
p_cap_giro_result = p_cap_giro['p_cap_giro'][p_cap_giro_index]
col1.metric(label="P/Cap. Giro", value=f"{p_cap_giro_result:.2f}")

# col2.11 - ebit dividido por ativos totais
ebit_ativo = df[df['papel'] == col1_selection]
ebit_ativo_index = int(ebit_ativo['Unnamed: 0'])
ebit_ativo_result = ebit_ativo['ebit_ativo'][ebit_ativo_index]
col2.metric(label="Ebit/Ativo", value=f"{ebit_ativo_result:.2f}")

# col1.12 - preço dividido pelos ativos circulantes líquidos por ação
p_ativo_circ_liq = df[df['papel'] == col1_selection]
p_ativo_circ_liq_index = int(p_ativo_circ_liq['Unnamed: 0'])
p_ativo_circ_liq_result = p_ativo_circ_liq['p_ativo_circ_liq'][p_ativo_circ_liq_index]
col1.metric(label="P/Ativ. Cir. liq.", value=f"{p_ativo_circ_liq_result:.2f}")

# col2.12 - roic
roic = df[df['papel'] == col1_selection]
roic_index = int(roic['Unnamed: 0'])
roic_result = roic['roic'][roic_index]
col2.metric(label="ROIC", value=f"{roic_result:.2f}%")

# col1.13 - dividend yield
div_yield = df[df['papel'] == col1_selection]
div_yield_index = int(div_yield['Unnamed: 0'])
div_yield_result = div_yield['div_yield'][div_yield_index]
col1.metric(label="Divd. Yield", value=f"{div_yield_result:.2f}%")

######

######
# Backtesting

data = datetime.today().strftime('%d-%m-%Y')
st.write("-----------------------------------------")
st.write( f" 🚦 Backtesting da Ação {col1_selection}" )
st.write( " 🚦 *Estratégia:* " ) 
st.write( " 🚦 Cruzamento de Médias Moveis (Rapida -> 17 / Lenta -> 72) " )
st.write( " 🚦 Intervalo utilizado -> Diário(Fechamento) " )
st.write(f" 🚦Periodo: 01-01-2020 até {data} ")

dados_back = vbt.YFData.download_symbol(f"{col1_selection}.SA", start="2020-01-01")
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
