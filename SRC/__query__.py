import __conectdb__
import __main__

delete_vazio_query = " DELETE FROM dados \
                              WHERE papel = ' ' OR papel IS NULL \
                                    OR tipo = ' ' OR tipo IS NULL \
                                    OR empresa = ' ' OR empresa IS NULL \
                                    OR cotacao = ' ' OR cotacao IS NULL \
                                    OR data_ult_cotacao IS NULL \
                                    OR min_52_sem = ' ' OR min_52_sem IS NULL \
                                    OR max_52_sem = ' ' OR max_52_sem IS NULL \
                                    OR vol_med_2m = ' ' OR vol_med_2m IS NULL \
                                    OR valor_mercado = ' ' OR valor_mercado IS NULL "

delete_dublicados_query = " DELETE FROM dados a USING (SELECT MAX(ctid) AS ctid, papel, data_ult_cotacao \
                                   FROM dados \
                                        GROUP BY papel, data_ult_cotacao HAVING COUNT(*) > 1) b \
                                                 WHERE a.papel = b.papel \
                                                       AND a.ctid <> b.ctid \
                                                       AND a.data_ult_cotacao = b.data_ult_cotacao \
                                                       AND a.ctid <> b.ctid "
