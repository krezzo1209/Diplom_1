import pytest
import requests
import allure
from helpers import generate_user_data, delete_user


@allure.suite("Тесты API: Пользователи")
@allure.feature("Создание пользователя")
class TestCreateUser:

    base_url = "https://stellarburgers.nomoreparties.site/api/v2"

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        # Генерируем уникальные данные
        payload = generate_user_data()

        response = requests.post(f"{self.base_url}/auth/register", json=payload)
        access_token = response.json().get("accessToken")

        # Удаляем пользователя после теста
        if access_token:
            delete_user(access_token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Нельзя создать уже существующего пользователя")
    def test_create_existing_user(self):
        # Регистрируем пользователя дважды
        payload = generate_user_data()
        requests.post(f"{self.base_url}/auth/register", json=payload)  # Первый раз — ок

        response = requests.post(f"{self.base_url}/auth/register", json=payload)  # Второй раз — ошибка

        delete_user(response.json().get("accessToken"))  # Удаляем, если токен есть

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert "такой пользователь уже существует" in response.json()["message"]

    @allure.title("Нельзя создать пользователя без email")
    def test_create_user_missing_email(self):
        payload = {
            "password": "password123",
            "name": "Иван"
        }

        response = requests.post(f"{self.base_url}/auth/register", json=payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert "email" in response.json()["message"].lower()