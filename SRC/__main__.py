import __conectdb__
#import __log__
import __list__
import backoff
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from datetime import date

RED   = "\033[1;31m"  
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
YELLOW = "\033[1;33m"

#@backoff.on_exception(backoff.expo,(Exception,TimeoutError), max_tries=10)
def dados():
    options = FirefoxOptions()
    #options.add_argument("--headless")
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

            time.sleep(2)
            web.find_element_by_xpath('/html/body/div[1]/div[1]/form/fieldset/input[1]').send_keys(i)
            web.find_element_by_xpath('/html/body/div[1]/div[1]/form/fieldset/input[2]').click()

            papel = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[2]/span')
            papel_text = papel.text

            #Insere os dados coletados no banco de dados#
            query_insert_bd = f" INSERT INTO dados VALUES ('{dt}','{papel_text}') "
            __conectdb__.in_dados(query_insert_bd)
            print(f"+{GREEN} dados da ação: {i}, gravados com sucesso {RESET}+")
            # --- #

dados()





        
