import __conectdb__
import __log__
import __list__
import backoff
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@backoff.on_exception(backoff.expo,(Exception,TimeoutError), max_tries=10)
def dados():
    options = FirefoxOptions()
    options.add_argument("--headless")
    web = webdriver.Firefox(options=options)

    web.implicitly_wait(20)

    url = 'https://fundamentus.com.br/'
    web.get(url)

    acao = __list__.list

    for i in acao:
        web.fin
