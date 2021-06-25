import dotenv
import os 
import psycopg2

dotenv.load_dotenv(dotenv.find_dotenv())

def conexao():
    con = psycopg2.connect(
        user = os.getenv('POSTGRES_USER'),
        password = os.getenv('POSTGRES_PASSWORD'),
        database = os.getenv('POSTGRES_DB'),
        host = 'localhost'
    )
    return con

def in_dados(query):
    vcon = conexao()
    c = vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
    
def se_dados(query):
    vcon = conexao()
    c = vcon.cursor()
    c.execute(query)
    rows = c.fetchall()  
    vcon.commit()
    vcon.close()
    return rows    