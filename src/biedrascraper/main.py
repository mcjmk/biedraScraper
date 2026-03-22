from biedrascraper import config
from biedrascraper.fetch import fetch_products_from_category
from biedrascraper.save import save_products_data


def main() -> None:
    print("STARTING")

    for url, category in zip(config.URLS, config.CATEGORIES, strict=True):
        print(f"Fetching products from {url}")
        products_data = fetch_products_from_category(url)
        print(f"Saving products to {category}")
        save_products_data(products_data, category=category)
        print(f"Finished {category}")


if __name__ == "__main__":
    main()
