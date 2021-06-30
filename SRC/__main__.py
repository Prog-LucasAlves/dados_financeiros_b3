import __conectdb__
#import __log__
import __list__
import backoff
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import datetime
from datetime import date, datetime

RED   = "\033[1;31m"  
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
YELLOW = "\033[1;33m"

#@backoff.on_exception(backoff.expo,(Exception,TimeoutError), max_tries=10)
def dados():
    options = FirefoxOptions()
    options.add_argument("--headless")
    web = webdriver.Firefox(options=options)

    web.implicitly_wait(20)

    url = 'https://fundamentus.com.br/'
    web.get(url)

    acao = __list__.lst_acao

    dt = date.today()

    for i in acao:
        #Consulta no bando de dados para verificar se os dados já se encontram no mesmo
        query_consult_bd = f" SELECT data_dado_inserido, papel \
                                    FROM dados \
                                        WHERE data_dado_inserido = '{dt}' \
                                            AND papel = '{i}' "
        result = __conectdb__.se_dados(query_consult_bd)
        # --- #

        if result != []:

            print(f"+{YELLOW} dados da ação: {i}, já cadastrados {RESET}+")

        else:    

            print(dt)

            time.sleep(2)
            web.find_element_by_xpath('/html/body/div[1]/div[1]/form/fieldset/input[1]').send_keys(i)
            web.find_element_by_xpath('/html/body/div[1]/div[1]/form/fieldset/input[2]').click()
            
            # Inicio da coleta dos dados #
            papel = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[2]/span')
            papel_text = papel.text
            #
            tipo = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[2]/td[2]/span')
            tipo_text = tipo.text
            #
            empresa = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[2]/span')
            empresa_text = empresa.text
            #
            setor = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[2]/span/a')
            setor_text = setor.text
            #
            cotação = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[4]/span')
            cotação_text = cotação.text.replace(',','.')
            #
            dt_ult_cotacao = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[2]/td[4]/span')
            dt_ult_cotacao_text = dt_ult_cotacao.text
            dt_ult_cotacao_tr = datetime.strptime(dt_ult_cotacao_text, '%d/%m/%Y').date()
            #
            min_52_sem = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[4]/span')
            min_52_sem_text = min_52_sem.text.replace(',','.')
            #
            max_52_sem = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[4]/span')
            max_52_sem_text = max_52_sem.text.replace(',','.')
            #

            #Insere os dados coletados no banco de dados#
            query_insert_bd = f" INSERT INTO dados VALUES ('{dt}','{papel_text}','{tipo_text}','{empresa_text}',\
            '{setor_text}','{cotação_text}','{dt_ult_cotacao_tr}','{min_52_sem_text}','{max_52_sem_text}') "
            __conectdb__.in_dados(query_insert_bd)
            print(f"+{GREEN} dados da ação: {i}, gravados com sucesso {RESET}+")
            # --- #

dados()