import mysql.connector
from mysql.connector import Error

def conectar_banco():
    """Função para conectar ao banco de dados."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',  # Altere conforme necessário
            user='admin',       # Usuário do banco de dados
            password='Str0ng@Passw0rd',  # Senha do banco
            database='estacionamento'   # Nome do banco
        )
        if conexao.is_connected():
            print("Conexão com o banco bem-sucedida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def buscar_carro_por_vaga(conexao, vaga):
    """Consulta o nome do carro para uma vaga específica."""
    try:
        cursor = conexao.cursor()
        query = "SELECT carro FROM carros WHERE vaga = %s"
        cursor.execute(query, (vaga,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else "Vaga vazia"
    except Error as e:
        print(f"Erro ao buscar carro para a vaga {vaga}: {e}")
        return "Erro"
