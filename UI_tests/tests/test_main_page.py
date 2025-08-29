import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    # Локаторы
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    ORDER_CARD = (By.CSS_SELECTOR, ".OrderHistory_card__2J5QI")
    ORDER_NUMBER = (By.CSS_SELECTOR, ".text.text_type_digits-default")
    MODAL_TITLE = (By.CSS_SELECTOR, ".Modal_modal__title__2s4mU")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close__2zc1h")

    @allure.step("Переходим в Конструктор")
    def click_constructor_link(self):
        self.click_element(self.CONSTRUCTOR_LINK)

    @allure.step("Кликаем по первому заказу в ленте")
    def click_first_order(self):
        self.click_element(self.ORDER_CARD)

    @allure.step("Проверяем, открыто ли модальное окно заказа")
    def is_order_modal_visible(self):
        return self.is_visible(self.MODAL_TITLE)

    @allure.step("Закрываем модальное окно заказа")
    def close_modal(self):
        self.click_element(self.CLOSE_MODAL_BUTTON)

    @allure.step("Ожидаем закрытия модального окна заказа")
    def wait_for_modal_close(self):
        return self.wait_for_invisibility(self.MODAL_TITLE)

    @allure.step("Получаем номер первого заказа из ленты")
    def get_first_order_number(self):
        return self.get_text(self.ORDER_NUMBER)
