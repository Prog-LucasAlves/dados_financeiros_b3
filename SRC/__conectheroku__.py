import psycopg2
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

def conexao():
    con = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE_URL"),
        host=os.getenv("HOST"),
    )
    return con

def in_dados(query):
    vcon = conexao()
    c = vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
   
