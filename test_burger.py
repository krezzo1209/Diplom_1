import pytest
import allure
from bun import Bun
from burger import Burger
from ingredient_types import Ingredient


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

    @allure.title("Проверка перемещения ингредиента")
    def test_move_ingredient(self, burger):
        # sauce = 0, filling = 1
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].name == "Мясо бессмертных моллюсков Protostomia"
        assert burger.ingredients[1].name == "Соус фирменный Space Sauce"

    @allure.title("Проверка пересчёта цены бургера")
    def test_price_calculation(self, burger):
        total_price = burger.get_price()
        assert total_price == 1255 * 2 + 80 + 1337

    @allure.title("Проверка генерации чека")
    def test_receipt_full_match(self, burger):
        expected_receipt = (
            f"(==== {burger.bun.name} ====)\n"
            f"= {burger.ingredients[0].type} {burger.ingredients[0].name} =\n"
            f"= {burger.ingredients[1].type} {burger.ingredients[1].name} =\n"
            f"(==== {burger.bun.name} ====)\n\n"
            f"Price: {burger.get_price()}\n"
        )
        assert burger.get_receipt() == expected_receipt
