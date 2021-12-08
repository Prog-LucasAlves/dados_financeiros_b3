import yfinance as yf
import pandas as pd
from datetime import date
from tqdm import tqdm

import __list__

df = pd.DataFrame()

inicio = '2000-01-01'
fim = date.today()

acao = __list__.lst_acao

for i in tqdm(acao):
    df = yf.download(f'{i}.SA', start=inicio, end=fim)
    df.to_csv(f'./precos/{i}.csv',sep=';')

ticker = 'BVSP'
df_b = yf.download(f'^{ticker}', start=inicio, end=fim)
df_b.to_csv(f'./precos/{ticker}.csv',sep=';')  