from flask import request
from flask_restful import Api, Resource

from app.core.base.typings import UserInputData
from app.adaptors.user_adaptor import UserAdaptor
from app.repositories import current_repo
from . import api


class UserV1Resource(Resource):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.adaptor = UserAdaptor(current_repo)

    def get(self, id: int):
        """
        개별 사용자 정보
        ---
        tags:
        - users
        responses:
          200:
            description: "Success"
        """
        user = self.adaptor.get(id)

        return user


class UserV1CollectionResource(Resource):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.adaptor = UserAdaptor(current_repo)

    def get(self):
        """
        사용자 목록
        ---
        tags:
        - users
        responses:
          200:
            description: "Success"
        """

        users = self.adaptor.get_list()
        return users

    def post(self):
        """
        사용자 생성
        ---
        tags:
        - users
        responses:
          200:
            description: "Success"
        """
        email = request.json.get("email")
        password = request.json.get("password")

        user = self.adaptor.create(UserInputData(email=email, password=password))
        return user


class CurrentUserV1Resource(Resource):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.adaptor = UserAdaptor(current_repo)

    def get(self):
        """
        현재 세션의 사용자 정보
        ---
        tags:
        - users
        responses:
          200:
            description: "Success"
        """
        user_id = request.headers["USER-ID"]
        user = self.adaptor.get(user_id)
        return user

    def put(self):
        """
        현재 세션의 사용자 정보 수정
        ---
        tags:
        - users
        responses:
          200:
            description: "Success"
        """
        user_id = request.headers["USER-ID"]
        email = request.json.get("email")
        password = request.json.get("password")
        user = self.adaptor.update(
            user_id, UserInputData(email=email, password=password)
        )
        return user


class UserAuthenticateV1Resource(Resource):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.adaptor = UserAdaptor(current_repo)

    def post(self):
        """
        사용자 인증
        email 과 password 를 통한 사용자 인증
        ---
        tags:
        - users
        responses:
          200:
            description: "Success"
        """
        email = request.json.get("email")
        password = request.json.get("password")
        user = self.adaptor.authenticate(email=email, password=password)

        return user


users_api = Api(api)
users_api.add_resource(UserV1Resource, "/v1.0/users/<int:id>", endpoint="user")
users_api.add_resource(UserV1CollectionResource, "/v1.0/users", endpoint="users")
users_api.add_resource(CurrentUserV1Resource, "/v1.0/users/self", endpoint="self")
users_api.add_resource(
    UserAuthenticateV1Resource, "/v1.0/users/authenticate", endpoint="authenticate"
)
