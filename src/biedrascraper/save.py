import json
from datetime import date
from typing import Literal, TypeAlias

import pandas as pd

ProductData: TypeAlias = list[tuple[str, float]]


def get_today_date() -> str:
    return date.today().strftime("%d-%m-%Y")


def get_today_filename() -> str:
    return f"biedra_{get_today_date()}"


def save_to_csv(products_data: ProductData) -> None:
    filename = f"{get_today_filename()}.csv"
    df = pd.DataFrame(products_data)
    df.to_csv(filename, index=False)
    print(f"Data extracted and successfully saved to {filename}.")


def save_to_excel(products_data: ProductData, category: str | None) -> None:
    filename = f"{get_today_filename()}.xlsx"
    sheet_name = category or "products"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df = pd.DataFrame(products_data)
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"{sheet_name} saved")

    print(f"Data extracted and successfully saved to {filename}.")


def save_to_json(products_data: ProductData) -> None:
    filename = f"{get_today_filename()}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(products_data, file)
    print(f"Data extracted and successfully saved to {filename}.")


def save_products_data(
    products_data: ProductData,
    *,
    format: Literal["excel", "csv", "json"] = "excel",
    category: str | None = None,
) -> None:
    if format == "excel":
        save_to_excel(products_data, category)
    elif format == "csv":
        save_to_csv(products_data)
    else:
        save_to_json(products_data)
