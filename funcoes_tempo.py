from datetime import datetime, timedelta

def calcular_tempo_restante(horario_saida):
    agora = datetime.now()
    try:
        saida = datetime.strptime(horario_saida, "%H:%M:%S").replace(year=agora.year, month=agora.month, day=agora.day)
    except ValueError:
        return "Inválido"

    if saida < agora:
        return "Expirado"



    tempo_restante = saida - agora
    horas, resto = divmod(tempo_restante.total_seconds(), 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}"

def timedelta_to_str(td):
    total_segundos = int(td.total_seconds())
    horas, resto = divmod(total_segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}"
