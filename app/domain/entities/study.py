from datetime import datetime, timedelta

class Study:
    def __init__(self, user_id, disciplina, conteudo, horas, minutos, dificuldade):
        self.user_id = user_id
        self.disciplina = disciplina
        self.conteudo = conteudo
        self.tempo_horas = horas
        self.tempo_minutos = minutos
        self.dificuldade = dificuldade
        self.criado_em = datetime.utcnow()

    def tempo_total_minutos(self):
        return self.tempo_horas * 60 + self.tempo_minutos

    def gerar_revisoes(self):
        """
        Retorna as datas das revisões D+1, D+7, D+14.
        """
        return [
            self.criado_em + timedelta(days=1),
            self.criado_em + timedelta(days=7),
            self.criado_em + timedelta(days=14),
        ]
