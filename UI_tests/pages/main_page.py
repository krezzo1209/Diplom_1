# pages/main_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    ORDER_FEED_LINK = (By.LINK_TEXT, "Лента заказов")
    FIRST_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::div[@class='card_root__LJvg2']")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BUN_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/preceding-sibling::p[@class='counter_counter__num__3CPl3']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.CLASS_NAME, "order-number")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, ".OrderHistory_text__2M82Z")

    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")

    def click_constructor_link(self):
        self.click_element(self.CONSTRUCTOR_LINK)

    def click_order_feed_link(self):
        self.click_element(self.ORDER_FEED_LINK)

    def click_first_ingredient(self):
        self.click_element(self.FIRST_INGREDIENT)

    def is_modal_visible(self):
        return self.is_visible(self.MODAL_TITLE)

    def close_modal(self):
        self.click_element(self.MODAL_CLOSE_BUTTON)

    def get_bun_counter(self):
        return int(self.get_text(self.BUN_COUNTER))

    def place_order(self):
        self.click_element(self.ORDER_BUTTON)

    def get_order_number(self):
        return int(self.get_text(self.ORDER_NUMBER))

    def get_total_orders(self):
        return int(self.get_text(self.TOTAL_ORDERS))

    def get_today_orders(self):
        return int(self.get_text(self.TODAY_ORDERS))

    def is_order_in_progress(self, number):
        orders = self.driver.find_elements(*self.IN_PROGRESS_ORDERS)
        return str(number) in [order.text for order in orders]