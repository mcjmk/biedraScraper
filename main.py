import time
from datetime import datetime

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By


def fetch_products(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(3)
    while True:
        try:
            more_button = driver.find_element(By.CSS_SELECTOR, '.infinite-trigger__button')
            driver.execute_script("arguments[0].scrollIntoView();", more_button)
            more_button.click()
            time.sleep(2)
        except (NoSuchElementException, ElementClickInterceptedException):
            break

    products = driver.find_elements(By.CLASS_NAME, 'product-grid__item')
    product_data = []
    for product in products:
        name_tag = product.find_element(By.CLASS_NAME, 'product-tile__name')
        product_name = name_tag.text.strip() if name_tag else "No name available"
        price_main_tag = product.find_element(By.CLASS_NAME, 'price-tile__sales')
        if price_main_tag:
            price_main = price_main_tag.text.split()[0]
            price_decimal_tag = product.find_element(By.CLASS_NAME, 'price-tile__decimal')
            price_decimal = price_decimal_tag.text.strip() if price_decimal_tag else "00"
            price_str = f"{price_main}.{price_decimal}"
            price = float(price_str)
        else:
            price = np.nan
        product_data.append((product_name, price))
        print(product_name, price)

    driver.quit()
    return product_data


if __name__ == '__main__':
    urls = [
        'https://zakupy.biedronka.pl/warzywa/',
        'https://zakupy.biedronka.pl/owoce/',
        'https://zakupy.biedronka.pl/mieso/',
        'https://zakupy.biedronka.pl/dania-gotowe/',
        'https://zakupy.biedronka.pl/napoje/',
        'https://zakupy.biedronka.pl/mrozone/',
        'https://zakupy.biedronka.pl/drogeria/',
        'https://zakupy.biedronka.pl/dla-domu/',
        'https://zakupy.biedronka.pl/dla-dzieci/',
        'https://zakupy.biedronka.pl/dla-zwierzat/',
        'https://zakupy.biedronka.pl/artykuly-spozywcze/'
    ]

    current_date = datetime.now().strftime("%d-%m-%Y")
    with pd.ExcelWriter('biedraCeny' + current_date + '.xlsx', engine='openpyxl') as writer:
        for url in urls:
            category = url.split('/')[-2]
            product_list = fetch_products(url)
            df = pd.DataFrame(product_list)
            df.to_excel(writer, sheet_name=category, index=False)
            print(f"{category} saved")
            print("Sleeping 10 seconds to not overuse the server...")
            time.sleep(10)

    print(f"Data extracted and saved to CSV file.")
