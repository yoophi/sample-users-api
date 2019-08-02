from flask_restful import Api, Resource

from app.adaptors import UserAdaptor
from app.core.repository.mem import UserRepository
from . import api


class UserResource(Resource):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.adaptor = UserAdaptor(UserRepository())

    def get(self, id):
        user = self.adaptor.get(id)

        return user


class UserCollectionResource(Resource):
    def get(self):
        pass

    def post(self):
        pass


class CurrentUserResource(Resource):
    def get(self):
        pass

    def put(self):
        pass


class AuthenticateUserResource(Resource):
    def post(self):
        pass


users_api = Api(api)
users_api.add_resource(UserResource, "/users/<int:id>", endpoint="user")
users_api.add_resource(UserCollectionResource, "/users", endpoint="users")
users_api.add_resource(CurrentUserResource, "/users/self", endpoint="self")
users_api.add_resource(
    AuthenticateUserResource, "/users/authenticate", endpoint="authenticate"
)
