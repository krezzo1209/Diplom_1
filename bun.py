import pytest
from praktikum.bun import Bun


@allure.suite("Unit: Bun")
class TestBun:

    @allure.title("Создание булочки с корректными параметрами")
    def test_bun_init(self):
        bun = Bun("Чёрная булка", 120.0)
        assert bun.name == "Чёрная булка"
        assert bun.price == 120.0

    @allure.title("Метод get_name возвращает имя булочки")
    def test_get_name(self):
        bun = Bun("Космическая булка", 150)
        assert bun.get_name() == "Космическая булка"

    @allure.title("Метод get_price возвращает цену булочки")
    def test_get_price(self):
        bun = Bun("Булка с антигравитацией", 200)
        assert bun.get_price() == 200

    @pytest.mark.parametrize("name, price", [
        ("white bun", 200),
        ("red bun", 300),
        ("black bun", 100),
    ])
    @allure.title("Параметризованный тест для разных булочек")
    def test_bun_get_price_parametrized(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
