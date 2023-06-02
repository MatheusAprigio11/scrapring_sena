from connect import con
from web import Web
cursor = con.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()

def listar_sorteio(marca):
    sql = f'SELECT * from {marca}'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas



##balbalbalbalçatesst
#learning git