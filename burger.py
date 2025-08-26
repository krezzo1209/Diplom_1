import pytest
import allure
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredient_mock():
    ing = Mock()
    ing.get_name.return_value = "cutlet"
    ing.get_price.return_value = 100
    ing.get_type.return_value = "FILLING"
    return ing


@allure.suite("Unit: Burger")
class TestBurger:

    @allure.title("Установка булочки")
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    @allure.title("Добавление ингредиента")
    def test_add_ingredient(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    @allure.title("Удаление ингредиента по индексу")
    def test_remove_ingredient(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title("Перемещение ингредиента")
    def test_move_ingredient(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        ing1, ing2 = Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ing2, ing1]

    @pytest.mark.parametrize("ingredient_price, expected_total", [
        (100, 300),
        (200, 400),
        (0, 200),
    ])
    @allure.title("Расчёт цены бургера")
    def test_get_price(self, bun_mock, ingredient_price, expected_total):
        ingredient = Mock()
        ingredient.get_price.return_value = ingredient_price
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_total

    @allure.title("Формирование чека")
    def test_get_receipt(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        expected_receipt = (
            f"(==== {bun_mock.get_name()} ====)\n"
            f"= filling {ingredient_mock.get_name()} =\n"
            f"(==== {bun_mock.get_name()} ====)\n\n
