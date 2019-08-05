from typing import Dict, List, Optional

from app.core.base.typings import UserInputData
from app.core.domain.user import User
from app.core.use_cases.user_list_use_case import UserUseCase


class UserAdaptor:
    def __init__(self, repo):
        self.use_case = UserUseCase(repo)

    def get_list(self, filters: Dict = None) -> List[User]:
        pass

    def get(self, id: int) -> Optional[User]:
        pass

    def create(self, data: UserInputData) -> User:
        pass

    def update(self, user_id: int, data: UserInputData) -> User:
        pass

    def authenticate(self, email: str, password: str) -> User:
        pass
