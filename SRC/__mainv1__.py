# This Python file uses the following encoding: utf-8

import __conectdb__
import __query__
import __check__
import __check_semana__
import __conectheroku__

# import __log__
import __list__
import backoff
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import date, datetime, timedelta
import logging
from tqdm import tqdm

# TODO #1 Criar Sheduler

# Cores utilizada no script
RED = "\033[1;31m"
GREEN = "\033[0;32m"
GREEN_T = "\033[92m"
RESET = "\033[0;0m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
GRAY = "\033[1;35m"

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@backoff.on_exception(backoff.expo, (NoSuchElementException), max_tries=10)
# Inicio da funcao para coleta dos dados
def dados():
    # Variável(dt) - responsavel por informar qual (x) dia sera feita a coleta dos dados
    # Ex.: dt = date.today() - timedelta(days=3) -> volta 3 dias atras no calendario
    dt = date.today() - timedelta(days=0)
    dt_sem = dt.weekday()
    # Variavel dt_dia_sem - responsavel por verificar qual e o dia da semana(Se for Sabado ou Domingo - nao havera coleta de dados)
    dt_dia_sem = __check_semana__.DIAS[dt_sem]
    dt = dt.strftime("%d/%m/%Y")
    # Faz a checagem se o dia da semana e Sabado ou Domingo
    if __check__.data_check != dt or dt_dia_sem == "Sábado" or dt_dia_sem == "Domingo":
        print(f"+{GRAY} Site não atualizado {RESET}+")
        print("--------------------------------------")
        print(f"Hoje é dia: {dt} - {dt_dia_sem} ")
        print(f"Data do site é: {__check__.data_check} - {__check__.day}")
        print("--------------------------------------")

    else:

        print(f"+{GREEN_T} Site atualizado vamos começar a coletar os dados. {RESET}+")
        # Faz checagem se a conexao com o banco de dados foi estabelecida
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
            options.page_load_strategy = "none"
            web = webdriver.Firefox(options=options)

            web.implicitly_wait(20)
            # Site utilizado para coleta dos dados
            url = "https://fundamentus.com.br/"
            web.get(url)
            # Variável (acao) - armazena uma lista com os tickers da acoes
            acao = __list__.lst_acao

            n = 0

            for i in tqdm(acao):

                try:

                    # Consulta no banco de dados para verificar se os dados já se encontram no mesmo (Ref.: data_ult_cotacao / papel)
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
                        os_dia = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[2]/span/font"
                            )
                            .text.replace("%", "")
                            .replace(",", ".")
                        )
                        #
                        pl = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        #
                        lpa = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        #
                        pvp = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[3]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        #
                        vpa = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[3]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        #
                        p_ebit = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        if len(p_ebit) <= 1:
                            p_ebit = 0
                        else:
                            p_ebit = p_ebit
                        #
                        marg_bruta = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(marg_bruta) <= 1:
                            marg_bruta = 0
                        else:
                            marg_bruta = marg_bruta
                        #
                        psr = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[5]/td[4]"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        if len(psr) <= 1:
                            psr = 0
                        else:
                            psr = psr
                        #
                        marg_ebit = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[5]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(marg_ebit) <= 1:
                            marg_ebit = 0
                        else:
                            marg_ebit = marg_ebit
                        #
                        p_ativo = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[6]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        if len(p_ativo) <= 1:
                            p_ativo = 0
                        else:
                            p_ativo = p_ativo
                        #
                        marg_liquida = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[6]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(marg_liquida) <= 1:
                            marg_liquida = 0
                        else:
                            marg_liquida = marg_liquida
                        #
                        p_cap_giro = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[7]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        if len(p_cap_giro) <= 1:
                            p_cap_giro = 0
                        else:
                            p_cap_giro = p_cap_giro
                        #
                        ebit_ativo = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[7]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(ebit_ativo) <= 1:
                            ebit_ativo = 0
                        else:
                            ebit_ativo = ebit_ativo
                        #
                        p_ativo_circ_liq = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[8]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("-", "0")
                        )
                        if len(p_ativo_circ_liq) <= 1:
                            p_ativo_circ_liq = 0
                        else:
                            p_ativo_circ_liq = p_ativo_circ_liq
                        #
                        roic = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[8]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(roic) <= 1:
                            roic = 0
                        else:
                            roic = roic
                        #
                        div_yield = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[9]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(div_yield) <= 1:
                            div_yield = 0
                        else:
                            div_yield = div_yield
                        #
                        roe = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[9]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(roe) <= 1:
                            roe = 0
                        else:
                            roe = roe
                        #
                        ev_ebitda = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[10]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        if len(ev_ebitda) <= 1:
                            ev_ebitda = 0
                        else:
                            ev_ebitda = ev_ebitda
                        #
                        liquidez_corr = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[10]/td[6]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        if len(liquidez_corr) <= 1:
                            liquidez_corr = 0
                        else:
                            liquidez_corr = liquidez_corr
                        #
                        ev_ebit = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[11]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                        )
                        if len(ev_ebit) <= 1:
                            ev_ebit = 0
                        else:
                            ev_ebit = ev_ebit
                        #
                        cres_rec = (
                            web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[3]/tbody/tr[12]/td[4]/span"
                            )
                            .text.replace(".", "")
                            .replace(",", ".")
                            .replace("%", "")
                        )
                        if len(cres_rec) <= 1:
                            cres_rec = 0
                        else:
                            cres_rec = cres_rec
                        #
                        ativo = web.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/table[4]/tbody/tr[2]/td[2]/span"
                        ).text.replace(".", "")
                        #
                        if setor == "Intermediários Financeiros":
                            disponibilidades = "0"
                            ativo_circulante = "0"
                            divd_bruta = "0"
                            divd_liquida = "0"
                            patr_liquido = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[3]/td[4]/span"
                            ).text.replace(".", "")
                        #
                        else:
                            disponibilidades = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[3]/td[2]/span"
                            ).text.replace(".", "")
                            #
                            ativo_circulante = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[4]/td[2]/span"
                            ).text.replace(".", "")
                            #
                            divd_bruta = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[2]/td[4]/span"
                            ).text.replace(".", "")
                            #
                            divd_liquida = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[3]/td[4]/span"
                            ).text.replace(".", "")
                            #
                            patr_liquido = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[4]/tbody/tr[4]/td[4]/span"
                            ).text.replace(".", "")
                            #
                            lucro_liquido_12m = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[5]/tbody/tr[5]/td[2]/span"
                            ).text.replace(".", "")
                            #
                            lucro_liquido_3m = web.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/table[5]/tbody/tr[5]/td[4]/span"
                            ).text.replace(".", "")
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

                        dt_h = date.today() - timedelta(days=0)
                        dt_ult_cotacao_h = datetime.strptime(
                            dt_ult_cotacao, "%d/%m/%Y"
                        ).date()
                        ult_balanco_pro_h = datetime.strptime(
                            ult_balanco_pro, "%d/%m/%Y"
                        ).date()
                        cotacao_h = cotacao.replace(",", ".")
                        min_52_sem_h = min_52_sem.replace(",", ".")
                        max_52_sem_h = max_52_sem.replace(",", ".")

                        query_insert_bd_h = f" INSERT INTO dados VALUES ( '{dt_h}','{papel}','{tipo}','{empresa}', \
                        '{setor}','{cotacao_h}','{dt_ult_cotacao_h}','{min_52_sem_h}','{max_52_sem_h}','{vol_med}', \
                        '{valor_mercado}','{valor_firma}','{ult_balanco_pro_h}','{nr_acoes}','{os_dia}','{pl}','{lpa}', \
                        '{pvp}','{vpa}','{p_ebit}','{marg_bruta}','{psr}','{marg_ebit}','{p_ativo}','{marg_liquida}', \
                        '{p_cap_giro}','{ebit_ativo}','{p_ativo_circ_liq}','{roic}','{div_yield}','{roe}', \
                        '{ev_ebitda}','{liquidez_corr}','{ev_ebit}','{cres_rec}','{ativo}','{disponibilidades}', \
                        '{ativo_circulante}','{divd_bruta}','{divd_liquida}','{patr_liquido}','{lucro_liquido_12m}', \
                        '{lucro_liquido_3m}' ) "
                        __conectheroku__.in_dados(query_insert_bd_h)

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
            __conectheroku__.in_dados(delete_vazio)

            # Removendo linhas(tabela dados) do BD duplicados (ref.: na coluna papel / data_ult_cotacao )
            delete_dublicados = __query__.delete_dublicados_query
            __conectdb__.in_dados(delete_dublicados)
            __conectheroku__.in_dados(delete_dublicados)

            # backup do banco de dados
            csv_file_name = "../Backup/some_file.csv"
            bk = __query__.backup_query
            with open(csv_file_name, "w") as f:
                __conectdb__.bk(bk, f)

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
