import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    ORDER_FEED_LINK = (By.LINK_TEXT, "Лента Заказов")
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    FIRST_INGREDIENT = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__text__3eUdz")
    MODAL_TITLE = (By.CSS_SELECTOR, ".Modal_modal__title__2s4mU")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close__2zc1h")
    BUN_COUNTER = (By.CSS_SELECTOR, ".counter_counter__num__3nue1")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    @allure.step("Переходим в ленту заказов")
    def click_order_feed_link(self):
        self.click_element(self.ORDER_FEED_LINK)

    @allure.step("Переходим в конструктор")
    def click_constructor_link(self):
        self.click_element(self.CONSTRUCTOR_LINK)

    @allure.step("Кликаем по первому ингредиенту")
    def click_first_ingredient(self):
        self.click_element(self.FIRST_INGREDIENT)

    @allure.step("Проверяем, открыто ли модальное окно")
    def is_modal_visible(self):
        return self.is_visible(self.MODAL_TITLE)

    @allure.step("Закрываем модальное окно")
    def close_modal(self):
        self.click_element(self.CLOSE_MODAL_BUTTON)

    @allure.step("Ожидаем, что модальное окно закроется")
    def wait_for_modal_close(self):
        return self.wait_for_invisibility(self.MODAL_TITLE)

    @allure.step("Получаем значение счётчика булки")
    def get_bun_counter(self):
        return int(self.get_text(self.BUN_COUNTER))

    @allure.step("Оформляем заказ")
    def place_order(self):
        self.click_element(self.PLACE_ORDER_BUTTON)
