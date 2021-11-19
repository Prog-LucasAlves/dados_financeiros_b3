import psycopg2
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

def conexao():
    """
    Função que tem o objetivo de de fazer a conexão com o banco de dados
    """
    con = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE_URL"),
        host=os.getenv("HOST"),
    )
    return con

def in_dados(query):
    """
    Função que tem o objetivo de realizar - INSERT / DELETE no banco de dados
    """
    vcon = conexao()
    c = vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
