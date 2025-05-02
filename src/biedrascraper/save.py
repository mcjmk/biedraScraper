import json
from datetime import date

import pandas as pd


def get_today_date():
    return date.today().strftime("%d-%m-%Y")


def get_today_filename():
    return f"biedra_{get_today_date()}"


def save_to_csv(products_data):
    filename = get_today_filename() + ".csv"
    df = pd.DataFrame(products_data)
    df.to_csv(filename, index=False)
    print(f"Data extracted and successfully saved to {filename}.")


def save_to_excel(products_data, category):
    filename = get_today_filename() + ".xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df = pd.DataFrame(products_data)
        df.to_excel(writer, sheet_name=category, index=False)
        print(f"{category} saved")

    print(f"Data extracted and successfully saved to {filename}.")


def save_to_json(products_data):
    filename = get_today_filename() + ".json"
    with open(filename, "w") as f:
        json.dump(products_data, f)
    print(f"Data extracted and successfully saved to {filename}.")


def save_products_data(products_data, format="excel", category=None):
    if format == "excel":
        save_to_excel(products_data, category)
    elif format == "csv":
        save_to_csv(products_data)
    elif format == "json":
        save_to_json(products_data)
