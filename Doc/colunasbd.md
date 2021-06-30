# Descrição das colunas do Banco de dados

- BD -> dados_financeiros

## Colunas

- (1) data_dado_inserido:
1. Descrição -> data em que o dado foi inserido no banco de dados. :white_check_mark:
2. Tipo(type) -> date

- (2) papel:
1. Descrição -> ticker da ação negociada na B3.
2. Tipo(type) -> varchar(255)

- (3) tipo:
1. Descrição -> tipo da ação(ON / PN / UNIT).
https://comoinvestir.thecap.com.br/diferenca-entre-acoes-preferenciais-ordinarias-units/
2. Tipo(Type) -> varchar(255)

- (4) empresa:
1. Descrição -> nome da empresa.
2. Tipo(Type) -> varchar(255)

- (5) setor:
1. Descrição -> setor em que a empresa atua
2. Tipo(type) -> varchar(255)

- (6) cotacao:
1. Descrição -> valor da ação no dia em que foi coletado os dado.
2. Tipo(type) -> money

- (7) data_ult_cotacao
1. Descrição -> data da última negociação da ação
2. Tipo(Type) -> date

- (8) min_52_sem:
1. Descrição -> menor valor da cotação em 52 semanas
2. Tipo(type) -> money

- (9) max_52_sem:
1. Descrição -> maior valor da cotação em 52 semanas
2. Tipo(type) -> money