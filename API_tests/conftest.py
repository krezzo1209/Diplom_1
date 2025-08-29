import pytest
from tests.helpers import generate_user_data, register_user, delete_user


@pytest.fixture
def new_user():
    """Фикстура: создаёт пользователя и удаляет после теста"""
    payload = generate_user_data()
    token = register_user(payload)
    yield payload, token
    delete_user(token)

