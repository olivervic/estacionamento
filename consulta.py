DIA_SEMANA_TRADUZIDO = {
    "Mon": "seg",
    "Tue": "ter",
    "Wed": "qua",
    "Thu": "qui",
    "Fri": "sex",
    "Sat": "sab",
    "Sun": "dom"
}


def buscar_carros_por_dia(conexao, dia_atual):
    try:
        cursor = conexao.cursor()
        query = """
        SELECT id, carro, placa, responsavel, horario_entrada, horario_saida, dia_semana, vaga
        FROM carros
        WHERE dia_semana LIKE %s
        """
        cursor.execute(query, (f"%{dia_atual}%",))
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar carros do dia {dia_atual}: {e}")
        return []


def buscar_carro_por_vaga(conexao, vaga):
    try:
        cursor = conexao.cursor()
        query = """
        SELECT carro, placa, responsavel, horario_entrada, horario_saida, dia_semana
        FROM carros
        WHERE vaga = %s
        """
        cursor.execute(query, (vaga,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar carros para a vaga {vaga}: {e}")
        return []

def buscar_vagas_por_usuario(conexao, usuario_id):
    try:
        cursor = conexao.cursor()
        query = """
        SELECT vaga
        FROM usuarios_vagas
        WHERE usuario_id = %s
        """
        cursor.execute(query, (usuario_id,))
        return [vaga[0] for vaga in cursor.fetchall()]
    except Exception as e:
        print(f"Erro ao buscar vagas para o usuário {usuario_id}: {e}")
        return []



def buscar_todos_carros(conexao):
    """Busca todos os carros na tabela 'carros'."""
    try:
        cursor = conexao.cursor()
        query = """
        SELECT carro, placa, responsavel, horario_entrada, horario_saida, dia_semana, vaga
        FROM carros
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar todos os carros: {e}")
        return []