mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"seu-email@dominio.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
base='light'\n\
primaryColor='#5d5c49'\n\
backgroundColor='#fbf6d0'\n\
secondaryBackgroundColor = '#fbf6d0'\n\
textColor='#0e1862'\n\

[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml