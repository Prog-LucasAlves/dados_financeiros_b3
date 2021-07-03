import __conectdb__
import __main__

delete_vazio_query = " DELETE FROM acao \
                              WHERE papel = ' ' OR papel IS NULL \
                                    OR tipo = ' ' OR tipo IS NULL \
                                    OR empresa = ' ' OR empresa IS NULL \
                                    OR cotacao = 0 OR cotacao IS NULL \
                                    OR data_ult_cotacao IS NULL \
                                    OR min_52_sem = 0 OR min_52_sem IS NULL \
                                    OR max_52_sem = 0 OR max_52_sem IS NULL \
                                    OR vol_med_2m = 0 OR vol_med_2m IS NULL \
                                    OR valor_mercado = 0 OR valor_mercado IS NULL \
                                    OR nr_acoes = 0 OR nr_acoes IS NULL \
                                    OR pl IS NULL "

delete_dublicados_query = " DELETE FROM acao a USING (SELECT MAX(ctid) AS ctid, papel, data_ult_cotacao \
                                   FROM acao \
                                        GROUP BY papel, data_ult_cotacao HAVING COUNT(*) > 1) b \
                                                 WHERE a.papel = b.papel \
                                                       AND a.ctid <> b.ctid \
                                                       AND a.data_ult_cotacao = b.data_ult_cotacao \
                                                       AND a.ctid <> b.ctid "
