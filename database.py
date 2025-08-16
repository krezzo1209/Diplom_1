import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_database_initialization():
    """
    Проверяем, что при создании объекта Database
    корректно инициализируются списки булочек и ингредиентов.
    """
    db = Database()
    assert len(db.buns) == 3
    assert len(db.ingredients) == 6


def test_available_buns_returns_correct_list():
    """
    Проверяем, что метод available_buns() возвращает список булочек.
    """
    db = Database()
    buns = db.available_buns()
    assert isinstance(buns, list)
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_name() == "white bun"
    assert buns[2].get_name() == "red bun"


def test_available_ingredients_returns_correct_list():
    """
    Проверяем, что метод available_ingredients() возвращает список ингредиентов.
    """
    db = Database()
    ingredients = db.available_ingredients()
    assert isinstance(ingredients, list)
    assert len(ingredients) == 6


@pytest.mark.parametrize("index, expected_name, expected_price", [
    (0, "hot sauce", 100),
    (1, "sour cream", 200),
    (2, "chili sauce", 300),
    (3, "cutlet", 100),
    (4, "dinosaur", 200),
    (5, "sausage", 300),
])
def test_ingredients_have_correct_data(index, expected_name, expected_price):
    """
    Параметризованный тест: проверяем, что ингредиенты имеют корректные имя и цену.
    """
    db = Database()
    ingredient = db.available_ingredients()[index]
    assert ingredient.get_name() == expected_name
    assert ingredient.get_price() == expected_price


@pytest.mark.parametrize("index, expected_type", [
    (0, INGREDIENT_TYPE_SAUCE),
    (1, INGREDIENT_TYPE_SAUCE),
    (2, INGREDIENT_TYPE_SAUCE),
    (3, INGREDIENT_TYPE_FILLING),
    (4, INGREDIENT_TYPE_FILLING),
    (5, INGREDIENT_TYPE_FILLING),
])
def test_ingredients_have_correct_type(index, expected_type):
    """
    Проверяем, что у ингредиентов правильный тип (SAUCE / FILLING).
    """
    db = Database()
    ingredient = db.available_ingredients()[index]
    assert ingredient.get_type() == expected_type