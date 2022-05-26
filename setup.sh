mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"seu-email@dominio.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
base='light'\n\
primaryColor='#5d5c49'\n\
backgroundColor='#FFD600'\n\
secondaryBackgroundColor = '#F0F2F6'\n\
textColor='#0e1862'\n\

[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml