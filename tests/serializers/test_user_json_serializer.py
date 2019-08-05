import json

from app.core.domain.user import User
from app.serializers.user import UserSchema


def test_serialize_domain_user():
    user = User(
        id=1,
        email='test@test.com',
        password='secret',
    )

    expected_json = """
        {
            "id": 1,
            "email": "test@test.com",
            "password": "secret"
        }
    """

    json_user = UserSchema().dumps(user).data
    assert json.loads(json_user) == json.loads(expected_json)
