from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
#options.add_argument("--headless")
check = webdriver.Firefox(options=options)

check.implicitly_wait(20)
    
url = "https://www.fundamentus.com.br/detalhes.php?papel=AALR3+"
check.get(url)

data_check = check.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr[2]/td[4]/span').text
check.quit()