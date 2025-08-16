import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def bun_mock():
    """
    Фикстура-мок для булочки.
    """
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredient_mock():
    """
    Фикстура-мок для ингредиента.
    """
    ing = Mock()
    ing.get_name.return_value = "cutlet"
    ing.get_price.return_value = 100
    ing.get_type.return_value = "FILLING"
    return ing


def test_set_buns(bun_mock):
    """
    Проверяем, что булочки устанавливаются корректно.
    """
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock


def test_add_ingredient(bun_mock, ingredient_mock):
    """
    Проверяем добавление ингредиента.
    """
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    assert ingredient_mock in burger.ingredients
    assert len(burger.ingredients) == 1


def test_remove_ingredient(bun_mock, ingredient_mock):
    """
    Проверяем удаление ингредиента по индексу.
    """
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient(bun_mock):
    """
    Проверяем перемещение ингредиента.
    """
    burger = Burger()
    burger.set_buns(bun_mock)

    ing1 = Mock()
    ing2 = Mock()
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    # Перемещаем первый ингредиент на вторую позицию
    burger.move_ingredient(0, 1)

    assert burger.ingredients[0] == ing2
    assert burger.ingredients[1] == ing1


@pytest.mark.parametrize("ingredient_price, expected_total", [
    (100, 300),  # 100*2 + 100 = 300
    (200, 400),  # 100*2 + 200 = 400
    (0, 200),    # 100*2 + 0 = 200
])
def test_get_price(bun_mock, ingredient_price, expected_total):
    """
    Проверяем расчёт цены бургера (с параметризацией).
    """
    ingredient = Mock()
    ingredient.get_price.return_value = ingredient_price

    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient)

    assert burger.get_price() == expected_total


def test_get_receipt(bun_mock, ingredient_mock):
    """
    Проверяем формирование чека.
    """
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)

    receipt = burger.get_receipt()

    # Проверяем наличие всех компонентов в чеке
    assert "(==== black bun ====)" in receipt
    assert "= filling cutlet =" in receipt.lower()
    assert f"Price: {burger.get_price()}" in receipt