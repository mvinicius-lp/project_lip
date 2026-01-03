from abc import ABC, abstractmethod
import datetime
from app.domain.entities.study import Study

class StudyRepository(ABC):

    @abstractmethod
    async def create(self, study: Study):
        pass

    @abstractmethod
    async def find_by_date(self, user_id: str, date: datetime): pass
