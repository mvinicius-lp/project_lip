from datetime import datetime

class Revision:
    def __init__(self, user_id, study_id, data_revisao):
        self.user_id = user_id
        self.study_id = study_id
        self.data_revisao = data_revisao
        self.realizada = False

    def marcar_realizada(self):
        self.realizada = True

    def esta_atrasada(self):
        return not self.realizada and datetime.utcnow() > self.data_revisao
