from abc import ABC, abstractmethod
from typing import Dict, Optional

from app.core.base.typings import UserInputData
from app.core.domain.user import User


class BaseRepository(ABC):
    @abstractmethod
    def get_list(self, filters: Dict = None):
        pass

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def create(self, user_data: UserInputData) -> User:
        pass

    @abstractmethod
    def update(self, id, user_data: UserInputData) -> User:
        pass

    @abstractmethod
    def authenticate(self, email: str, password: str) -> Optional[User]:
        pass
