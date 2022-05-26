mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"seu-email@dominio.com\"\n\
" > ~/.streamlit/credentials.toml

echo 
"[theme]
primaryColor=' #020202 '
backgroundColor=' #c4c3c3 '
secondaryBackgroundColor=' #ebd316 '
font = 'sans serif'
[servidor]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml