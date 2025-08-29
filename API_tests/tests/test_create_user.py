import pytest
import requests
import allure
from tests.data import ERROR_MESSAGES


@allure.suite("API: Пользователи")
class TestCreateUser:

    base_url = "https://stellarburgers.nomoreparties.site/api/v2"

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, new_user):
        payload, token = new_user
        response = requests.post(f"{self.base_url}/auth/register", json=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Нельзя создать уже существующего пользователя")
    def test_create_existing_user(self, new_user):
        payload, _ = new_user
        response = requests.post(f"{self.base_url}/auth/register", json=payload)

        assert response.status_code == 403
        assert ERROR_MESSAGES["user_exists"] in response.json()["message"]

    @allure.title("Нельзя создать пользователя без обязательных полей")
    @pytest.mark.parametrize("payload, missing_field", [
        ({"password": "123456", "name": "Ivan"}, "email"),
        ({"email": "ivan@ya.ru", "name": "Ivan"}, "password"),
        ({"email": "ivan@ya.ru", "password": "123456"}, "name"),
    ])
    def test_create_user_missing_field(self, payload, missing_field):
        response = requests.post(f"{self.base_url}/auth/register", json=payload)

        assert response.status_code == 403
        assert ERROR_MESSAGES["missing_field"].lower() in response.json()["message"].lower()
