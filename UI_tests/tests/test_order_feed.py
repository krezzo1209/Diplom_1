import allure
from pages.order_feed_page import OrderFeedPage


@allure.suite("UI: Лента заказов")
class TestOrderFeed:

    @allure.title("Проверка, что страница Ленты заказов открывается")
    def test_order_feed_page_opens(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        assert page.is_order_feed_page_opened()

    @allure.title("Проверка отображения заказов в ленте")
    def test_orders_are_displayed_in_feed(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        assert page.is_orders_list_visible()

    @allure.title("Проверка отображения счётчика 'Выполнено за всё время'")
    def test_total_orders_counter_displayed(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        assert page.is_total_orders_counter_visible()

    @allure.title("Проверка отображения счётчика 'Выполнено за сегодня'")
    def test_today_orders_counter_displayed(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        assert page.is_today_orders_counter_visible()

    @allure.title("Клик по заказу открывает модальное окно")
    def test_click_order_opens_modal(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        page.click_first_order()
        assert page.is_order_modal_opened()

    @allure.title("Закрытие модального окна заказа по крестику")
    def test_close_order_modal_with_cross(self, driver):
        page = OrderFeedPage(driver)
        page.open()
        page.click_first_order()
        assert page.is_order_modal_opened()
        page.close_order_modal()
        assert page.is_order_modal_closed()
