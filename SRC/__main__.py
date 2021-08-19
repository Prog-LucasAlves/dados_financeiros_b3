import __conectdb__
import __query__
import __check__
import __check_semana__

# import __log__
import __list__
import backoff
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import date, timedelta

RED = "\033[1;31m"
GREEN = "\033[0;32m"
GREEN_T = "\033[92m"
RESET = "\033[0;0m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
GRAY = "\033[1;35m"


@backoff.on_exception(backoff.expo, (NoSuchElementException), max_tries=2)
def dados():

    dt = date.today() - timedelta(days=0)
    dt_sem = dt.weekday()
    dt_dia_sem = __check_semana__.DIAS[dt_sem]
    dt = dt.strftime("%d/%m/%Y")

    if __check__.data_check != dt or dt_dia_sem == "Sábado" or dt_dia_sem == "Domingo":
        print(f"+{GRAY} Site não atualizado {RESET}+")
        print("--------------------------------------")
        print(f"Hoje é dia: {dt} - {dt_dia_sem} ")
        print(f"Data do site é: {__check__.data_check} - {__check__.day}")
        print("--------------------------------------")

    else:

        print(f"+{GREEN_T} Site atualizado vamos começar a coletar os dados. {RESET}+")

        if __conectdb__.verifica_conexao() == False:
            return print(
                f""" 
+{RED} Conexão não estabelecida com o Banco de Dados, verifique: {RESET}+
-{RED} Docker {RESET} 
            """
            )

        else:
            print(
                f"""
+{GREEN_T} Conexão estabelecida com sucesso ao Banco de Dados. {RESET}+ """
            )
            print("-------------------------------------------------------")

            inicio = time.time()

            options = FirefoxOptions()
            options.add_argument("--headless")
            web = webdriver.Firefox(options=options)

            web.implicitly_wait(20)

            url = "https://fundamentus.com.br/"
            web.get(url)

            acao = __list__.lst_acao

            n = 0

            for i in acao:

                try:

                    # Consulta no bando de dados para verificar se os dados já se encontram no mesmo (Ref.: data_ult_cotacao / papel)
                    query_consult_bd = f" SELECT data_dado_inserido, papel \
                                                FROM dados \
                                                    WHERE data_ult_cotacao = '{dt}' \
                                                        AND papel = '{i}' "
                    result = __conectdb__.se_dados(query_consult_bd)
                    # --- #

                    if result != []:

                        print(f"+{YELLOW} Dados da ação: {i}, já cadastrados {RESET}+")

                    else:

                        time.sleep(2)
                        web.find_element_by_xpath(
                            "/html/body/div[1]/div[1]/form/fieldset/input[1]"
                        ).send_keys(i)
                        web.find_element_by_xpath(
                            "/html/body/div[1]/div[1]/form/fieldset/input[2]"
                        ).click()

                        # Inicio da coleta dos dados #
                        time.sleep(2)
                        papel = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[2]/span"
                        ).text
                        #
                        tipo = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[2]/td[2]/span"
                        ).text
                        #
                        empresa = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[2]/span"
                        ).text
                        #
                        setor = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[2]/span/a"
                        ).text
                        #
                        cotacao = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[4]/span"
                        ).text
                        #
                        dt_ult_cotacao = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[2]/td[4]/span"
                        ).text
                        #
                        min_52_sem = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[4]/span"
                        ).text
                        #
                        max_52_sem = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[4]/span"
                        ).text
                        #
                        vol_med = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[1]/tbody/tr[5]/td[4]/span"
                        ).text.replace(".", "")
                        #
                        valor_mercado = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[2]/tbody/tr[1]/td[2]/span"
                        ).text.replace(".", "")
                        #
                        valor_firma = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[2]/tbody/tr[2]/td[2]/span"
                        ).text.replace(".", "")
                        #
                        ult_balanco_pro = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[2]/tbody/tr[1]/td[4]/span"
                        ).text
                        #
                        nr_acoes = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[2]/tbody/tr[2]/td[4]/span"
                        ).text.replace(".", "")
                        #
                        os_dia = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[2]/span/font"
                        ).text.replace("%", "").replace(",", ".")
                        #
                        pl = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".")
                        #
                        lpa = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".")
                        #
                        pvp = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[3]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".")
                        #
                        vpa = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[3]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        p_ebit = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        marg_bruta = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        psr = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[5]/td[4]"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        marg_ebit = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[5]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        p_ativo = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[6]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        marg_liquida = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[6]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        p_cap_giro = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[7]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        ebit_ativo = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[7]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        p_ativo_circ_liq = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[8]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        roic = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[8]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        div_yield = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[9]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        roe = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[9]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        ev_ebitda = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[10]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        liquidez_corr = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[10]/td[6]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        ev_ebit = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[11]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("-", "0")
                        #
                        cres_rec = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[3]/tbody/tr[12]/td[4]/span"
                        ).text.replace(".", "").replace(",", ".").replace("%", "").replace("-", "0")
                        #
                        ativo = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[4]/tbody/tr[2]/td[2]/span"
                        ).text.replace(".","")
                        #
                        if setor == 'Intermediários Financeiros':
                            disponibilidades = '0'
                            ativo_circulante = '0'
                            divd_bruta = '0'
                            divd_liquida = '0'
                            patr_liquido = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[3]/td[4]/span"
                        ).text
                        #
                        else: 
                            disponibilidades = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[3]/td[2]/span"
                            ).text.replace(".","")
                        #
                            ativo_circulante = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[4]/td[2]/span"
                            ).text.replace(".","")
                        #
                            divd_bruta = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[2]/td[4]/span"
                            ).text.replace(".","")
                        #
                            divd_liquida = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[3]/td[4]/span"
                            ).text.replace(".","")
                        #
                            patr_liquido = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[4]/td[4]/span"
                            ).text.replace(".","")
                        #
                            lucro_liquido_12m = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[5]/tbody/tr[5]/td[2]/span"
                            ).text.replace(".","")
                        #    
                            lucro_liquido_3m = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[5]/tbody/tr[5]/td[4]/span"
                            ).text.replace(".","")
                        #    
                        # Insere os dados coletados no banco de dados #
                        query_insert_bd = f" INSERT INTO dados VALUES ( '{dt}','{papel}','{tipo}','{empresa}', \
                        '{setor}','{cotacao}','{dt_ult_cotacao}','{min_52_sem}','{max_52_sem}','{vol_med}', \
                        '{valor_mercado}','{valor_firma}','{ult_balanco_pro}','{nr_acoes}','{os_dia}','{pl}','{lpa}', \
                        '{pvp}','{vpa}','{p_ebit}','{marg_bruta}','{psr}','{marg_ebit}','{p_ativo}','{marg_liquida}', \
                        '{p_cap_giro}','{ebit_ativo}','{p_ativo_circ_liq}','{roic}','{div_yield}','{roe}', \
                        '{ev_ebitda}','{liquidez_corr}','{ev_ebit}','{cres_rec}','{ativo}','{disponibilidades}', \
                        '{ativo_circulante}','{divd_bruta}','{divd_liquida}','{patr_liquido}','{lucro_liquido_12m}', \
                        '{lucro_liquido_3m}' ) "
                        __conectdb__.in_dados(query_insert_bd)
                        print(
                            f"+{GREEN} Dados da ação: {i}, gravados com sucesso {RESET}+"
                        )
                        # --- #

                        n += 1
                except (TypeError):
                    print(TypeError)
                    print(f"+{RED} Dados da ação: {i}, não gravados {RESET} +")
                    pass

            # Removendo linhas(tabela dados) do BD com valores vazios (ref.: na coluna papel)
            delete_vazio = __query__.delete_vazio_query
            __conectdb__.in_dados(delete_vazio)

            # Removendo linhas(tabela dados) do BD duplicados (ref.: na coluna papel / data_ult_cotacao )
            delete_dublicados = __query__.delete_dublicados_query
            __conectdb__.in_dados(delete_dublicados)

            # Finalizando o Navegador
            web.quit()

            fim = time.time()
            hours, rem = divmod(fim - inicio, 3600)
            minutes, seconds = divmod(rem, 60)

            # Fim
            print(f"{RED}-----------------{RESET}")
            print(f"{BLUE}Finalizou. {n} Empresas Cadastradas")
            print(
                "Tempo: {:0>2}:{:0>2}:{:05.2f}".format(
                    int(hours), int(minutes), seconds
                )
            )
            print(f"{RESET}{RED}-----------------{RESET}")


dados()
