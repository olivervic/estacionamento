import mysql.connector
from mysql.connector import Error
from consulta import *

def conectar_banco():
    """Função para conectar ao banco de dados."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',  # Altere conforme necessário
            #host='195.200.5.69',  # Altere conforme necessário
            user='phpmy',       # Usuário do banco de dados
            #user='root',       # Usuário do banco de dados
            password='odahviing',  # Senha do banco
            database='estacionamentovic',   # Nome do banco
            #port=32768
        )
        if conexao.is_connected():
            print("Conexão com o banco bem-sucedida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None