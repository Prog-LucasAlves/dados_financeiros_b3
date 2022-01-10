'''
Descrição:
Esse código pega os dados das cotações das empresas listadas na bolsa brasileira e armazena cada ação com os dados coletados em um arquivo .csv

Coleta também os dados da cotações do índice bovespa e armazena os dados coletados em um arquivo .csv

Local: pasta(precos)
'''

# Bibliotecas utilizadas
import yfinance as yf
import pandas as pd
from datetime import date
from tqdm import tqdm

# Lista com o nome das ações
import __list__

df = pd.DataFrame()

inicio = '2000-01-01'
fim = date.today()

acao = __list__.lst_acao

# Coletando as cotações das ações
for i in tqdm(acao):
    df = yf.download(f'{i}.SA', start=inicio, end=fim, progress=False, threads=False)
    df.to_csv(f'./precos/{i}.csv',sep=';')

# Coletando as cotações do índice bovespa
ticker = 'BVSP'
df_b = yf.download(f'^{ticker}', start=inicio, end=fim, progress=False, threads=False)
df_b.to_csv(f'./precos/{ticker}.csv',sep=';')  


