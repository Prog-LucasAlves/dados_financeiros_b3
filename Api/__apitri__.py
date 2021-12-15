import pandas as pd
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import requests
import numpy as np

import __list__


# Lista com o nome das ações
acao = __list__.lst_acao

for i in tqdm(acao):
    url = f'https://www.fundamentus.com.br/resultados_trimestrais.php?papel={i}&tipo=1'
    hearder = {'user-agent':'Mozilla/5.0'}
    ret1 = requests.get(url, headers=hearder)
    soup1 = bs(ret1.text, 'html.parser')

    df = soup1.td.string.find_all_next
    #rr = soup1.td[1].string

    # Coletando os nomes das colunas
    column_headers = soup1.findAll('tr')[0]
    column_headers = [i.getText() for i in column_headers.findAll('th')]

    # Coletando os dados das colunas
    rows = soup1.findAll('tr')[1:]
    df_dados = []
    for h in range(len(rows)):
        df_dados.append([col.getText() for col in rows[h].findAll('td')])

        # Coletando o link do documento
        rows1 = soup1.findAll('tr')[1:]
        lista_link = []
        for t in range(len(rows1)):
            for link in rows1[t].find_all('a'):
                lista_link.append(link.get('href'))   
    
    lista_df = []
    for a in lista_link:
        if 'NumeroSequencialDocumento' in a:
            lista_df.append(a)

    lista_rr = []
    for b in lista_link:
        if 'Tela=ext&numProtocolo' in b:
            lista_rr.append(b) 

    # Adicionando os dados coletados em um DataFrame
    data = pd.DataFrame(df_dados, columns=column_headers[:])
    data['Demonstração Financeira'] = lista_df
    data['Release de Resultados'] = pd.Series(lista_rr)

    # Salavando os dados em um arquivo .csv
    data.to_csv(f'../Api/trimestre/{i}.csv', sep=';') 