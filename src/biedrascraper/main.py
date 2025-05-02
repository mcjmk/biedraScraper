from biedrascraper import config
from biedrascraper.fetch import fetch_products_from_category
from biedrascraper.save import save_products_data


def main():
    print("STARTING")

    for URL, CATEGORY in zip(config.URLS, config.CATEGORIES):
        print(f"Fetching products from {URL}")
        products_data = fetch_products_from_category(URL)
        print(f"Saving products to {CATEGORY}")
        save_products_data(products_data, CATEGORY)
        print(f"Finished {CATEGORY}")
        # print(products_data)


if __name__ == "__main__":
    main()
