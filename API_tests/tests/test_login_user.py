import requests
import allure
from tests.data import ERROR_MESSAGES


@allure.suite("API: Авторизация")
class TestLoginUser:

    base_url = "https://stellarburgers.nomoreparties.site/api/v2"

    @allure.title("Успешный вход с корректными данными")
    def test_login_existing_user(self, new_user):
        payload, _ = new_user
        response = requests.post(f"{self.base_url}/auth/login", json={
            "email": payload["email"],
            "password": payload["password"]
        })

        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Ошибка входа с неверным паролем")
    def test_login_with_wrong_password(self, new_user):
        payload, _ = new_user
        response = requests.post(f"{self.base_url}/auth/login", json={
            "email": payload["email"],
            "password": "wrongpass"
        })

        assert response.status_code == 401
        assert ERROR_MESSAGES["unauthorized"] in response.json()["message"]

    @allure.title("Ошибка входа с несуществующим email")
    def test_login_with_unknown_email(self):
        response = requests.post(f"{self.base_url}/auth/login", json={
            "email": "unknown@ya.ru",
            "password": "password123"
        })

        assert response.status_code == 401
        assert ERROR_MESSAGES["unauthorized"] in response.json()["message"]
