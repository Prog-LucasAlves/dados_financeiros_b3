mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"seu-email@dominio.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

echo "\
[theme]\n\
# Primary accent for interactive elements
primaryColor = '#7792E3'
# Background color for the main content area
backgroundColor = '#273346'
# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'
# Color used for almost all text
textColor = '#FFFFFF'
# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: 'sans serif'
font = 'sans serif'
" > ~/.streamlit/config.toml