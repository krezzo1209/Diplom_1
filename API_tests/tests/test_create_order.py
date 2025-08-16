import pytest
import requests
import allure
from helpers import generate_user_data, register_user, delete_user, get_ingredients


@allure.suite("Тесты API: Заказы")
@allure.feature("Создание заказа")
class TestCreateOrder:

    base_url = "https://stellarburgers.nomoreparties.site/api/v2"

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized_with_ingredients(self):
        # Регистрация
        payload = generate_user_data()
        token = register_user(payload)

        # Получаем ингредиенты
        ingredients = get_ingredients()
        bun_id = next(i["id"] for i in ingredients if i["type"] == "bun")
        filling_id = next(i["id"] for i in ingredients if i["type"] == "main")

        response = requests.post(
            f"{self.base_url}/orders",
            headers={"Authorization": token},
            json={"ingredients": [bun_id, filling_id, bun_id]}
        )

        delete_user(token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self):
        ingredients = get_ingredients()
        bun_id = next(i["id"] for i in ingredients if i["type"] == "bun")
        filling_id = next(i["id"] for i in ingredients if i["type"] == "main")

        response = requests.post(
            f"{self.base_url}/orders",
            json={"ingredients": [bun_id, filling_id, bun_id]}
        )

        assert response.status_code == 200  # Даже без авторизации можно создать заказ
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_empty_ingredients(self):
        payload = generate_user_data()
        token = register_user(payload)

        response = requests.post(
            f"{self.base_url}/orders",
            headers={"Authorization": token},
            json={"ingredients": []}
        )

        delete_user(token)

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert "Ingredient ids must be provided" in response.json()["message"]

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_hash(self):
        payload = generate_user_data()
        token = register_user(payload)

        response = requests.post(
            f"{self.base_url}/orders",
            headers={"Authorization": token},
            json={"ingredients": ["invalid_hash_123"]}
        )

        delete_user(token)

        assert response.status_code == 500  # Ожидается ошибка сервера при неверных ID