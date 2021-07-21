# Descrição das colunas do Banco de dados

- BD -> dados_financeiros

## Colunas

- (1) data_dado_inserido:
1. Descrição -> data em que o dado foi inserido no banco de dados. :white_check_mark:
2. Tipo(type) -> date

- (2) papel:
1. Descrição -> Código da ação.
2. Tipo(type) -> varchar(255)

- (3) tipo:
1. Descrição -> tipo da ação(ON / PN / UNIT).
https://comoinvestir.thecap.com.br/diferenca-entre-acoes-preferenciais-ordinarias-units/
2. Tipo(Type) -> varchar(255)

- (4) empresa:
1. Descrição -> Nome comercial da empresa.
2. Tipo(type) -> varchar(255)

- (5) setor:
1. Descrição -> Classificação setorial.
2. Tipo(type) -> varchar(255)

- (6) cotacao:
1. Descrição -> Cotação de fechamento da ação.
2. Tipo(type) -> money

- (7) data_ult_cotacao
1. Descrição -> data do último pregão em que o ativo foi negociada.
2. Tipo(type) -> date

- (8) min_52_sem:
1. Descrição -> menor cotação da ação nos últimos 12 meses
2. Tipo(type) -> money

- (9) max_52_sem:
1. Descrição -> maior cotação da ação nos últimos 12 meses
2. Tipo(type) -> money

- (10) vol_med(2m):
1. Descrição -> volume médio de negociações da ação nos últimos 2 meses.
2. Tipo(type) -> money

- (11) valor_mercado:
1. Descrição -> valor de mercado da empresa - Calculando multiplicando o preço da ação pelo número total de ações.
2. Tipo(type) -> money

- (12) valor_firma:
1. Descrição -> Valor da firma(Enterprise Value) é calculado somando o valor de mercado da empresa a sua dívida líquida.
2. Tipo(type) -> money

- (13) ult_balanco_pro:
1. Descrição -> Data do último balanço processado pela empresa.
2. Tipo(type) -> date

- (14) nr_acoes:
1. Descrição -> Número total de ações somadas(ON / PN / UNIT)
2. Tipo(type) -> integer

- (15) os_dia:
1. Descrição -> Oscilação da ação no dia da coleta dos dados
2. Tipo(type) -> double precision