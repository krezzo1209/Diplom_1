import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://stellarburgers.nomoreparties.site"

    def open(self):
        with allure.step(f"Открываем страницу {self.url}"):
            self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        with allure.step(f"Ищем элемент {locator}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

    def click_element(self, locator):
        with allure.step(f"Кликаем по элементу {locator}"):
            element = self.find_element(locator)
            element.click()

    def get_text(self, locator):
        with allure.step(f"Получаем текст элемента {locator}"):
            return self.find_element(locator).text

    def is_visible(self, locator, timeout=10):
        with allure.step(f"Проверяем, что элемент {locator} видим на странице"):
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )

    def wait_for_invisibility(self, locator, timeout=10):
        with allure.step(f"Ожидаем исчезновения элемента {locator}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
