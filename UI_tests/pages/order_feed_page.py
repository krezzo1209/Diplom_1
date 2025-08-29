# pages/order_feed_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By


class OrderFeedPage(BasePage):
    ORDER_HISTORY = (By.CSS_SELECTOR, ".OrderHistory_text__2M82Z")
    ORDER_NUMBER = (By.CLASS_NAME, "order-number")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")

    def get_all_orders(self):
        return self.driver.find_elements(*self.ORDER_HISTORY)

    def get_total_orders_count(self):
        return int(self.get_text(self.TOTAL_ORDERS))

    def get_today_orders_count(self):
        return int(self.get_text(self.TODAY_ORDERS))