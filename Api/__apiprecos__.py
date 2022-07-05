'''
Descrição:
Esse código pega os dados das cotações das empresas listadas na bolsa brasileira e armazena cada ação com os dados coletados em um arquivo .csv

Coleta também os dados da cotações do índice bovespa e armazena os dados coletados em um arquivo .csv

Local: pasta(precos)
'''

# Bibliotecas utilizadas
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date
from tqdm import tqdm
import logging

# Lista com o nome das ações
import __list__

logging.basicConfig(filename='./log/espc.log', level=logging.DEBUG, format='%(asctime)s :: %(levelname)s :: %(filename)s :: %(lineno)d')

df = pd.DataFrame()

inicio = '2010-01-01'
fim = date.today()

acao = __list__.lst_acao
indices = __list__.lst_indices
crypto = __list__.lst_crypto
moedas = __list__.lst_moedas

# Coletando as cotações das ações

for i in tqdm(acao):
    df = yf.download(f'{i}.SA', start=inicio, end=fim, progress=False, threads=False)
    # Média Movel 200P
    df['MM200'] = df['Adj Close'].rolling(200).mean()
    # Indicador Mayer
    df['Mayer'] = df['Adj Close'] / df['MM200']
    # Indicador IFR
    df['Variation'] = df['Adj Close'].diff()
    df['Gain'] = np.where(df['Variation'] > 0, df['Variation'], 0) 
    df['Loss'] = np.where(df['Variation'] < 0, df['Variation'], 0) 
    n = 14 # define window interval
    simple_avg_gain = df['Gain'].rolling(n).mean()
    simple_avg_loss = df['Loss'].abs().rolling(n).mean()
    classic_avg_gain = simple_avg_gain.copy()
    classic_avg_loss = simple_avg_loss.copy()
    for f in range(n, len(classic_avg_gain)):
        classic_avg_gain[f] = (classic_avg_gain[f - 1] * (n - 1) + df['Gain'].iloc[f]) / n
        classic_avg_loss[f] = (classic_avg_loss[f - 1] * (n - 1) + df['Loss'].abs().iloc[f]) / n
    df['Simple RS'] = simple_avg_gain / simple_avg_loss
    df['Classic RS'] = classic_avg_gain / classic_avg_loss
    df['Simple RSI'] = 100 - (100 / (1 + df['Simple RS']))
    df['Classic RSI'] = 100 - (100 / (1 + df['Classic RS']))


    df.to_csv(f'./precos/{i}.csv',sep=';')
    logging.info('Preços das ações salvos com SUCESSO')

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

# Função para calcular o retorno(Índices)
def calcula_retono_indices():
    for i in indices:
        df = pd.read_csv(f'./indices/{i}.csv', sep=';')
        df['Retornos'] = round(df['Adj Close'].pct_change() * 100, 2)
        df.to_csv(f'./indices/{i}.csv', sep=';')

# Função para calcular o retorno(Crypto)
def calcula_retorno_crypto():
    for i in crypto:
        df = pd.read_csv(f'./crypto/{i}.csv', sep=';')
        df['Retornos'] = round(df['Adj Close'].pct_change() * 100, 2)
        df.to_csv(f'./crypto/{i}.csv', sep=';')

# Função para calcular o retorno(Moedas)
def calcula_retorno_moedas():
    for i in moedas:
        df = pd.read_csv(f'./moedas/{i}.csv', sep=';')
        df['Retornos'] = round(df['Adj Close'].pct_change() * 100, 2)
        df.to_csv(f'./moedas/{i}.csv', sep=';')

if __name__ == "__main__":
    calcula_retono_indices()
    calcula_retorno_crypto()
    calcula_retorno_moedas()

#####