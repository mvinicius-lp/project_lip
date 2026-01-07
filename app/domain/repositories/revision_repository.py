from abc import ABC, abstractmethod
import datetime
from app.domain.entities.revision import Revision

class RevisionRepository(ABC):

    @abstractmethod
    async def create(self, revision: Revision): pass
    
    @abstractmethod
    async def find_by_date(self, user_id: str, date: datetime): pass

    @abstractmethod
    async def find_future(self, user_id: str, date: datetime): pass

    @abstractmethod
    async def find_past(self, user_id: str, date: datetime): pass

    
