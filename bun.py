import pytest
from praktikum.bun import Bun


def test_bun_init():
    """
    Проверяем, что булочка корректно создаётся с заданными именем и ценой.
    """
    bun = Bun("Чёрная булка", 120.0)
    assert bun.name == "Чёрная булка"
    assert bun.price == 120.0


def test_get_name():
    """
    Проверяем, что метод get_name возвращает корректное имя булочки.
    """
    bun = Bun("Космическая булка", 150)
    assert bun.get_name() == "Космическая булка"


def test_get_price():
    """
    Проверяем, что метод get_price возвращает корректную цену булочки.
    """
    bun = Bun("Булка с антигравитацией", 200)
    assert bun.get_price() == 200


@pytest.mark.parametrize("name, price", [
    ("white bun", 200),
    ("red bun", 300),
    ("black bun", 100),
])
def test_bun_get_price_parametrized(name, price):
    """
    Параметризованный тест для проверки разных булочек из базы данных.
    """
    bun = Bun(name, price)
    assert bun.get_price() == price