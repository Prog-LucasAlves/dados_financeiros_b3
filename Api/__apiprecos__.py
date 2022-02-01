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
indices = __list__.lst_indices
crypto = __list__.lst_crypto
moedas = __list__.lst_moedas

# Coletando as cotações das ações
for i in tqdm(acao):
    df = yf.download(f'{i}.SA', start=inicio, end=fim, progress=False, threads=False)
    df.to_csv(f'./precos/{i}.csv',sep=';')

# Coletando as cotações de alguns índices 
for i in tqdm(indices):
    df_b = yf.download(f'^{i}', start=inicio, end=fim, progress=False, threads=False)
    df_b.to_csv(f'./indices/{i}.csv', sep=';') 

# Coletando as cotações de algumas crypto
for i in tqdm(crypto):
    df_crypto = yf.download(f'{i}', start=inicio, end=fim, progress=False, threads=False)
    df_crypto.to_csv(f'./crypto/{i}.csv', sep=';')

for i in tqdm(moedas):
    df_moedas = yf.download(f'{i}', start=inicio, end=fim, progress=False, threads=False)
    df_moedas.to_csv(f'./moedas/{i}.csv', sep=';')

# Função para calcular o retorno
def calcula_retono_indices():
    for i in indices:
        df = pd.read_csv(f'./indices/{i}.csv', sep=';')
        df['Retornos'] = round(df['Adj Close'].pct_change() * 100, 2)
        df.to_csv(f'./indices/{i}.csv', sep=';')

# Função para calcular o retorno
def calcula_retorno_crypto():
    for i in crypto:
        df = pd.read_csv(f'./crypto/{i}.csv', sep=';')
        df['Retornos'] = round(df['Adj Close'].pct_change() * 100, 2)
        df.to_csv(f'./crypto/{i}.csv', sep=';')

# Funçaõ para calcular o retonor
def calcula_retorno_moedas():
    for i in moedas:
        df = pd.read_csv(f'./moedas/{i}.csv', sep=';')
        df['Retornos'] = round(df['Adj Close'].pct_change() * 100, 2)
        df.to_csv(f'./moedas/{i}.csv', sep=';')

calcula_retono_indices()
calcula_retorno_crypto()
calcula_retorno_moedas()
