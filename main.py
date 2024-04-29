import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.by import By
import openpyxl

def fetch_products(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(5)
    while True:
        try:
            more_button = driver.find_element(By.CSS_SELECTOR, '.infinite-trigger__button')
            driver.execute_script("arguments[0].scrollIntoView();", more_button)  # Przewijanie do przycisku
            more_button.click()
            time.sleep(2)
        except (NoSuchElementException, ElementClickInterceptedException):
            break
    current_date = datetime.now().strftime("%d-%m-%Y")

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
            price = f"{price_main}.{price_decimal}({current_date})"
        else:
            price = "Price not available"

        product_data.append((product_name, price))
        print(product_name, price)

    driver.quit()
    return product_data


if __name__ == '__main__':
    urls = \
        ['https://zakupy.biedronka.pl/warzywa/', 'https://zakupy.biedronka.pl/owoce/', 'https://zakupy.biedronka.pl/mieso/',
         'https://zakupy.biedronka.pl/dania-gotowe/', 'https://zakupy.biedronka.pl/napoje/',
         'https://zakupy.biedronka.pl/mrozone/', 'https://zakupy.biedronka.pl/drogeria/',
         'https://zakupy.biedronka.pl/dla-domu/', 'https://zakupy.biedronka.pl/dla-dzieci/',
         'https://zakupy.biedronka.pl/dla-zwierzat/', 'https://zakupy.biedronka.pl/artykuly-spozywcze/',
         'https://zakupy.biedronka.pl/dania-gotowe/']

    writer = pd.ExcelWriter('products.xlsx', engine='openpyxl')

    for url in urls[0:3]:
        category = url.split('/')[-2]
        product_list = fetch_products(url)
        df = pd.DataFrame(product_list)
        df.to_excel(writer, sheet_name=category, index=False)

        filename = f'products_{category}.csv'
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Price'])
            for data in product_list:
                writer.writerow(data)
        print(f"Data extracted and saved to {filename} for category {category}.")
        time.sleep(10)
        print("Sleeping 10 seconds...")
    print(f"Data extracted and saved to CSV file.")
