import pytest
import requests
import allure
from helpers import generate_user_data, register_user, delete_user


@allure.suite("Тесты API: Авторизация")
@allure.feature("Вход пользователя")
class TestLoginUser:

    base_url = "https://stellarburgers.nomoreparties.site/api/v2"

    @allure.title("Успешный вход с корректными данными")
    def test_login_existing_user(self):
        # Регистрируем и логиним
        payload = generate_user_data()
        register_user(payload)

        response = requests.post(f"{self.base_url}/auth/login", json={
            "email": payload["email"],
            "password": payload["password"]
        })

        # Удаляем пользователя
        delete_user(response.json().get("accessToken"))

        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Ошибка входа с неверным паролем")
    def test_login_with_wrong_password(self):
        payload = generate_user_data()
        register_user(payload)

        response = requests.post(f"{self.base_url}/auth/login", json={
            "email": payload["email"],
            "password": "wrongpass"
        })

        delete_user(response.json().get("accessToken"))

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert "или пароль" in response.json()["message"]

    @allure.title("Ошибка входа с несуществующим email")
    def test_login_with_unknown_email(self):
        response = requests.post(f"{self.base_url}/auth/login", json={
            "email": "unknown@ya.ru",
            "password": "password123"
        })

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert "или пароль" in response.json()["message"]