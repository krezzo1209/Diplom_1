import allure
from pages.main_page import MainPage


@allure.suite("UI: Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчики заказов увеличиваются после оформления заказа")
    def test_order_counters_increase(self, driver):
        page = MainPage(driver)
        page.open()

        with allure.step("Добавляем ингредиент и оформляем заказ"):
            page.click_first_ingredient()
            page.place_order()

        with allure.step("Ждём закрытия модального окна заказа"):
            page.wait_for_invisibility(page.ORDER_NUMBER)

        with allure.step("Проверяем, что счётчики увеличились"):
            assert page.get_total_orders() > 0
            assert page.get_today_orders() > 0

        with allure.step("Проверяем, что заказ появился в списке 'В работе'"):
            order_number = page.get_order_number()
            assert page.is_order_in_progress(order_number)
