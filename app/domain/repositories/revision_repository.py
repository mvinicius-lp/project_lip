from abc import ABC, abstractmethod
from app.domain.entities.revision import Revision

class RevisionRepository(ABC):

    @abstractmethod
    async def create(self, revision: Revision):
        pass
