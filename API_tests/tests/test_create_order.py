import requests
import allure
from tests.helpers import get_ingredients
from tests.data import ERROR_MESSAGES


@allure.suite("API: Заказы")
class TestCreateOrder:

    base_url = "https://stellarburgers.nomoreparties.site/api/v2"

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized(self, new_user):
        _, token = new_user
        ingredients = get_ingredients()
        bun = next(i["_id"] for i in ingredients if i["type"] == "bun")
        filling = next(i["_id"] for i in ingredients if i["type"] == "main")

        response = requests.post(
            f"{self.base_url}/orders",
            headers={"Authorization": token},
            json={"ingredients": [bun, filling, bun]}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self):
        ingredients = get_ingredients()
        bun = next(i["_id"] for i in ingredients if i["type"] == "bun")
        filling = next(i["_id"] for i in ingredients if i["type"] == "main")

        response = requests.post(
            f"{self.base_url}/orders",
            json={"ingredients": [bun, filling, bun]}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_empty_ingredients(self, new_user):
        _, token = new_user
        response = requests.post(
            f"{self.base_url}/orders",
            headers={"Authorization": token},
            json={"ingredients": []}
        )

        assert response.status_code == 400
        assert ERROR_MESSAGES["empty_ingredients"] in response.json()["message"]

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_invalid_hash(self, new_user):
        _, token = new_user
        response = requests.post(
            f"{self.base_url}/orders",
            headers={"Authorization": token},
            json={"ingredients": ["invalid_hash"]}
        )

        assert response.status_code == 500
