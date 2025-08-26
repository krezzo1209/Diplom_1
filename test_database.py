import pytest
import allure
from src.main.java.ru.praktikum.Database import Database
from src.main.java.ru.praktikum.Bun import Bun
from src.main.java.ru.praktikum.Ingredient import Ingredient


@allure.suite("Unit-тесты: Database")
class TestDatabase:

    @allure.title("База должна содержать хотя бы одну булочку и один ингредиент")
    def test_database_not_empty(self):
        with allure.step("Получаем тестовую базу"):
            db = Database()

        with allure.step("Проверяем, что в базе есть булочки"):
            buns = db.available_buns()
            assert isinstance(buns, list)
            assert all(isinstance(b, Bun) for b in buns)
            assert len(buns) > 0

        with allure.step("Проверяем, что в базе есть ингредиенты"):
            ingredients = db.available_ingredients()
            assert isinstance(ingredients, list)
            assert all(isinstance(i, Ingredient) for i in ingredients)
            assert len(ingredients) > 0

    @allure.title("Проверяем корректность данных в базе")
    def test_database_content(self):
        db = Database()

        with allure.step("Проверяем булочки"):
            bun_names = [bun.get_name() for bun in db.available_buns()]
            assert "black bun" in bun_names
            assert "white bun" in bun_names

        with allure.step("Проверяем ингредиенты"):
            ingredient_names = [i.get_name() for i in db.available_ingredients()]
            assert "hot sauce" in ingredient_names
            assert "cutlet" in ingredient_names
            assert "cheese" in ingredient_names
