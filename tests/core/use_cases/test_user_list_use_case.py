from unittest import mock

import pytest

from app.core.domain.user import User
from app.core.request_objects.user_list_request_object import UserListRequestObject
from app.core.response_objects import ResponseFailure
from app.core.use_cases.user_list_use_case import UserListUseCase


@pytest.fixture
def domain_users():
    user_1 = User(
        id=1,
        email="test1@test.com",
        password="secret1"
    )
    user_2 = User(
        id=2,
        email="test2@test.com",
        password="secret2"
    )
    user_3 = User(
        id=3,
        email="test3@test.com",
        password="secret3"
    )
    user_4 = User(
        id=4,
        email="test4@test.com",
        password="secret4"
    )

    return [user_1, user_2, user_3, user_4]


def test_user_list_with_parameters(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    user_list_use_case = UserListUseCase(repo)
    request = UserListRequestObject()
    response_object = user_list_use_case.execute(request)

    assert bool(response_object) is True
    repo.list.assert_called_with()
    assert response_object.value == domain_users


def test_user_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    user_list_use_case = UserListUseCase(repo)
    request_object = UserListRequestObject.from_dict({})
    response_object = user_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }