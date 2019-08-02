from typing import NamedTuple

from app.core.use_cases.user_list_use_case import UserUseCase


class UserInputData(NamedTuple):
    email: str
    password: str


class UserData(NamedTuple):
    id: int
    email: str


class UserAdaptor:
    def __init__(self, repo):
        self.use_case = UserUseCase(repo)

    def get_list(self, filters):
        pass

    def get(self, id):
        pass

    def create(self, data):
        pass
