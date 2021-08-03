# Descrição das colunas do Banco de dados

## Nome do banco de dados -> dados_financeiros

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

- (16) pl:
1. Descrição -> Preço da ação dividido pelo lucro por ação
2. Tipo(type) -> double precision

- (17) lpa:
1. Descrição -> Lucro por ação
2. Tipo(type) -> double precision

- (18) pvp:
1. Descrição -> Preço da ação dividido pelo valor patrimonial por ação
2. Tipo(type) -> double precision

- (19) vpa: Valor Patrimonial por Ação
1. Descrição -> Valor do patrimônio líquido dividido pelo número total de ações
2. Tipo(type) -> double precision

- (20) p_ebit: 
1. Descrição -> Preço da ação dividido pelo ebit por ação
2. Tipo(type) -> double precision

- (21) marg_bruta:
1. Descrição -> Lucro bruto dividido pela receita líquida
2. Tipo(type) -> double precision

- (22) psr:
1. Descrição -> Preço da ação dividido pela receita líquida por ação
2. Tipo(type) -> double precision

- (23) marg_ebit:
1. Descrição -> Ebit dividido pela receita líquida
2. Tipo(type) -> double precision

- (24) p_ativos:
1. Descrição -> Preço da ação dividido pelos ativos totais por ação
2. Tipo(type) -> double precision
   
- (25) marg_liquida:
1. Descrição -> Lucro líquido dividido pela receita líquida
2. Tipo(type) -> double precision