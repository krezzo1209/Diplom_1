import pytest
import allure
from src.main.java.ru.praktikum.Ingredient import Ingredient


@allure.suite("Unit-тесты: Ingredient")
class TestIngredient:

    @allure.title("Проверка создания ингредиента и его свойств")
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("sauce", "chili sauce", 50),
        ("filling", "beef", 200),
        ("sauce", "ketchup", 30)
    ])
    def test_create_ingredient(self, ingredient_type, name, price):
        with allure.step("Создаём ингредиент"):
            ingredient = Ingredient(ingredient_type, name, price)

        with allure.step("Проверяем свойства"):
            assert ingredient.get_type() == ingredient_type
            assert ingredient.get_name() == name
            assert ingredient.get_price() == price
