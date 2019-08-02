from app.core.domain.user import User


def test_user_model_init():
    user = User(id=1, email='test@test.com', password='secret')
    assert user.id == 1
    assert user.email == 'test@test.com'
    assert user.password == 'secret'


def test_user_from_dict():
    user = User.from_dict({
        'id': 1,
        'email': 'test@test.com',
        'password': 'secret',
    })
    assert user.id == 1
    assert user.email == 'test@test.com'
    assert user.password == 'secret'


def test_user_to_dict():
    user_dict = {
        'id': 1,
        'email': 'test@test.com',
        'password': 'secret',
    }
    user = User.from_dict(user_dict)
    assert user.to_dict() == user_dict


def test_user_comparison():
    user_dict = {
        'user_id': 1,
        'email': 'test@test.com',
        'password': 'secret',
    }
    user1 = User.from_dict(user_dict)
    user2 = User.from_dict(user_dict)

    assert user1 == user2
