import __conectdb__
#import __log__
import __list__
import backoff
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

#@backoff.on_exception(backoff.expo,(Exception,TimeoutError), max_tries=10)
def dados():
    options = FirefoxOptions()
    #options.add_argument("--headless")
    web = webdriver.Firefox(options=options)

    web.implicitly_wait(20)

    url = 'https://fundamentus.com.br/'
    web.get(url)

    acao = __list__.lst_acao

    for i in acao:

        time.sleep(2)
        web.find_element_by_xpath('/html/body/div[1]/div[1]/form/fieldset/input[1]').send_keys(i)
        web.find_element_by_xpath('/html/body/div[1]/div[1]/form/fieldset/input[2]').click()

        papel = web.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[2]/span')
        papel_text = papel.text
        print(papel_text)

        query_insert_bd = f" INSERT INTO dados VALUES ('{papel_text}') "

        #query_d = " INSERT INTO acao VALUES ( '"+papel_text+"',
        __conectdb__.in_dados(query_insert_bd)

dados()





        
