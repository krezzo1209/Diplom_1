import allure
from pages.main_page import MainPage


@allure.suite("UI: Главная страница")
class TestMainPage:

    @allure.title("Переход в Конструктор из Ленты заказов")
    def test_click_constructor_link(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_order_feed_link()
        page.click_constructor_link()
        assert "constructor" in page.get_current_url()

    @allure.title("Переход в Ленту заказов")
    def test_click_order_feed_link(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_order_feed_link()
        assert "feed" in page.get_current_url()

    @allure.title("Открытие модального окна ингредиента")
    def test_click_ingredient_opens_modal(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_first_ingredient()
        assert page.is_modal_visible()

    @allure.title("Закрытие модального окна по крестику")
    def test_close_modal_with_cross(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_first_ingredient()
        assert page.is_modal_visible()
        page.close_modal()
        page.wait_for_modal_close()

    @allure.title("Счётчик увеличивается при добавлении ингредиента")
    def test_counter_increases_when_adding_ingredient(self, driver):
        page = MainPage(driver)
        page.open()
        initial_counter = page.get_bun_counter()
        page.click_first_ingredient()
        page.place_order()
        new_counter = page.get_bun_counter()
        assert new_counter == initial_counter + 1
