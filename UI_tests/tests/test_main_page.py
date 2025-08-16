import pytest
from pages.main_page import MainPage


def test_click_constructor_link(driver):
    page = MainPage(driver)
    page.open()
    page.click_order_feed_link()  # Уйти в ленту
    page.click_constructor_link()  # Вернуться в конструктор
    assert "constructor" in driver.current_url


def test_click_order_feed_link(driver):
    page = MainPage(driver)
    page.open()
    page.click_order_feed_link()
    assert "feed" in driver.current_url


def test_click_ingredient_opens_modal(driver):
    page = MainPage(driver)
    page.open()
    page.click_first_ingredient()
    assert page.is_modal_visible()


def test_close_modal_with_cross(driver):
    page = MainPage(driver)
    page.open()
    page.click_first_ingredient()
    assert page.is_modal_visible()
    page.close_modal()
    assert not page.is_modal_visible()


def test_counter_increases_when_adding_ingredient(driver):
    page = MainPage(driver)
    page.open()
    initial_counter = page.get_bun_counter()
    page.click_first_ingredient()  # Добавляем булочку
    page.place_order()  # Оформляем заказ
    new_counter = page.get_bun_counter()
    assert new_counter == initial_counter + 1