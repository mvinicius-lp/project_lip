from datetime import date, timedelta

class UserStreak:
    def __init__(self, user_id: str, current_streak: int, last_activity_date: date):
        self.user_id = user_id
        self.current_streak = current_streak
        self.last_activity_date = last_activity_date

    def register_activity(self, today: date):
        if self.last_activity_date == today:
            return  

        if self.last_activity_date == today - timedelta(days=1):
            self.current_streak += 1
        else:
            self.current_streak = 1

        self.last_activity_date = today
