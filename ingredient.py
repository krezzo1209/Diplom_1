import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_ingredient_init():
    """
    Проверяем, что ингредиент корректно создаётся с типом, именем и ценой.
    """
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert ingredient.type == INGREDIENT_TYPE_SAUCE
    assert ingredient.name == "hot sauce"
    assert ingredient.price == 100


def test_get_name():
    """
    Проверяем, что get_name() возвращает корректное имя.
    """
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
    assert ingredient.get_name() == "dinosaur"


def test_get_price():
    """
    Проверяем, что get_price() возвращает корректную цену.
    """
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
    assert ingredient.get_price() == 200


def test_get_type():
    """
    Проверяем, что get_type() возвращает корректный тип ингредиента.
    """
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    assert ingredient.get_type() == INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (INGREDIENT_TYPE_FILLING, "sausage", 300),
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
])
def test_ingredient_get_price_parametrized(ingredient_type, name, price):
    """
    Параметризованный тест: проверяем разные ингредиенты.
    """
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price
    assert ingredient.get_name() == name
    assert ingredient.get_type() == ingredient_type