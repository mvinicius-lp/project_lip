from abc import ABC, abstractmethod
from app.domain.entities.study import Study

class StudyRepository(ABC):

    @abstractmethod
    async def create(self, study: Study):
        pass
