import pytest
import allure
from src.burger import Burger
from src.bun import Bun
from src.ingredient_types import Ingredient


@allure.suite("Unit: Burger")
class TestBurger:

    @pytest.fixture
    def burger(self):
        burger = Burger()
        burger.set_buns(Bun("Краторная булка", 1255))
        burger.add_ingredient(Ingredient("sauce", "Соус фирменный Space Sauce", 80))
        burger.add_ingredient(Ingredient("filling", "Мясо бессмертных моллюсков Protostomia", 1337))
        return burger

    @allure.title("Проверка добавления ингредиента")
    def test_add_ingredient(self, burger):
        assert len(burger.ingredients) == 2

    @allure.title("Проверка удаления ингредиента")
    def test_remove_ingredient(self, burger):
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    @allure.title("Проверка пересчёта цены бургера")
    def test_price_calculation(self, burger):
        total_price = burger.get_price()
        assert total_price == 1255 * 2 + 80 + 1337

    @allure.title("Проверка генерации чека")
    def test_receipt_contains_bun_and_ingredient(self, burger):
        receipt = burger.get_receipt()
        assert "Краторная булка" in receipt
        assert "Соус фирменный Space Sauce" in receipt

