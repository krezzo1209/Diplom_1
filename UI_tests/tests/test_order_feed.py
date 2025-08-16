def test_order_counters_increase(driver):
    page = MainPage(driver)
    page.open()

    # Добавляем ингредиент и оформляем заказ
    page.click_first_ingredient()
    page.place_order()

    # Ждём закрытия модального окна
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "order-number"))
    )

    # Проверяем счётчики
    assert page.get_total_orders() > 0
    assert page.get_today_orders() > 0

    # Проверяем, что заказ в работе
    order_number = page.get_order_number()
    assert page.is_order_in_progress(order_number)