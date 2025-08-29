import allure
from pages.order_feed_page import OrderFeedPage


@allure.suite("UI: Лента заказов")
class TestOrderFeed:

    @allure.title("Переход в Конструктор из Ленты заказов")
    def test_click_constructor_link_from_feed(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        page.click_constructor_link()
        assert "constructor" in page.get_current_url()

    @allure.title("Открытие модального окна заказа")
    def test_click_order_opens_modal(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        page.click_first_order()
        assert page.is_order_modal_visible()

    @allure.title("Закрытие модального окна заказа по крестику")
    def test_close_order_modal_with_cross(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        page.click_first_order()
        assert page.is_order_modal_visible()
        page.close_modal()
        page.wait_for_modal_close()

    @allure.title("Проверка отображения номера заказа в ленте")
    def test_order_number_displayed_in_feed(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        order_number = page.get_first_order_number()
        assert order_number.isdigit(), "Номер заказа должен состоять из цифр"
