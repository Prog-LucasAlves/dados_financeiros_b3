mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"seu-email@dominio.com\"\n\
" > ~/.streamlit/credentials.toml

echo 
"[theme]
primaryColor = '#84a3a7'
backgroundColor = '#7b9971'
secondaryBackgroundColor = '#fafafa'
textColor= '#424242'
font = 'sans serif'

[servidor]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml