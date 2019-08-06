from typing import Optional, Dict

from app.core.base.typings import UserInputData
from app.core.base.repository import BaseRepository
from app.core.domain.user import User


class MemRepo(BaseRepository):

    def get_list(self, filters: Dict = None):
        pass

    def get(self, id: int):
        pass

    def create(self, user_data: UserInputData) -> User:
        pass

    def update(self, id, user_data: UserInputData) -> User:
        pass

    def authenticate(self, email: str, password: str) -> Optional[User]:
        pass
