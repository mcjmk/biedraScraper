import time
from typing import TypeAlias

import numpy as np
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ProductData: TypeAlias = list[tuple[str, float]]


def show_all_products(driver: webdriver.Chrome) -> None:
    while True:
        try:
            more_button = driver.find_element(By.CSS_SELECTOR, ".infinite-trigger__button")
            driver.execute_script(
                "arguments[0].scrollIntoView();",
                more_button,
            )
            more_button.click()
            time.sleep(2)
        except (
            NoSuchElementException,
            ElementClickInterceptedException,
        ):
            break
        except Exception as e:
            print(f"Error showing all products: {e}")
            break


def fetch_products_from_category(url: str) -> ProductData:
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        driver.implicitly_wait(3)

        show_all_products(driver)

        products = driver.find_elements(By.CLASS_NAME, "product-grid__item")
        product_data: ProductData = []
        for product in products:
            name_tag = product.find_element(By.CLASS_NAME, "product-tile__name")
            product_name = name_tag.text.strip() or "No name available"

            try:
                price_main_tag = product.find_element(By.CLASS_NAME, "price-tile__sales")
                price_main = price_main_tag.text.split()[0]
                price_decimal_tag = product.find_element(By.CLASS_NAME, "price-tile__decimal")
                price_decimal = price_decimal_tag.text.strip() or "00"
                price = float(f"{price_main}.{price_decimal}")
            except NoSuchElementException:
                price = np.nan

            product_data.append((product_name, price))
            print(product_name, price)

        return product_data
    finally:
        driver.quit()
