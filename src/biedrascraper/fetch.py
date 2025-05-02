import time

import numpy as np
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def fetch_products_from_category(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(3)

    while True:
        try:
            more_button = driver.find_element(
                By.CSS_SELECTOR, ".infinite-trigger__button"
            )
            driver.execute_script(
                "arguments[0].scrollIntoView();", more_button
            )
            more_button.click()
            time.sleep(2)
        except (NoSuchElementException, ElementClickInterceptedException):
            break

    products = driver.find_elements(By.CLASS_NAME, "product-grid__item")
    product_data = []
    for product in products:
        name_tag = product.find_element(By.CLASS_NAME, "product-tile__name")
        product_name = (
            name_tag.text.strip() if name_tag else "No name available"
        )
        price_main_tag = product.find_element(
            By.CLASS_NAME, "price-tile__sales"
        )
        if price_main_tag:
            price_main = price_main_tag.text.split()[0]
            price_decimal_tag = product.find_element(
                By.CLASS_NAME, "price-tile__decimal"
            )
            price_decimal = (
                price_decimal_tag.text.strip() if price_decimal_tag else "00"
            )
            price_str = f"{price_main}.{price_decimal}"
            price = float(price_str)
        else:
            price = np.nan

        product_data.append((product_name, price))
        print(product_name, price)

    driver.quit()
    return product_data
