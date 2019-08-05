from app.core.domain.user import User


def test_user_model_init():
    USER_ID = 1
    USER_EMAIL = "test@test.com"
    USER_PASSWORD = "secret"

    user = User(id=USER_ID, email=USER_EMAIL, password=USER_PASSWORD)
    assert user.id == USER_ID
    assert user.email == USER_EMAIL
    assert user.password == USER_PASSWORD


def test_user_from_dict():
    USER_ID = 1
    USER_EMAIL = "test@test.com"
    USER_PASSWORD = "secret"

    user = User.from_dict(
        {"id": USER_ID, "email": USER_EMAIL, "password": USER_PASSWORD}
    )

    assert user.id == USER_ID
    assert user.email == USER_EMAIL
    assert user.password == USER_PASSWORD


def test_user_to_dict():
    user_dict = {"id": 1, "email": "test@test.com", "password": "secret"}
    user = User.from_dict(user_dict)
    assert user.to_dict() == user_dict


def test_user_comparison():
    user_dict = {"user_id": 1, "email": "test@test.com", "password": "secret"}
    user1 = User.from_dict(user_dict)
    user2 = User.from_dict(user_dict)

    assert user1 == user2
