URL: str = "https://zakupy.biedronka.pl/"

CATEGORIES: list[str] = [
    "warzywa",
    # "owoce",
    # "piekarnia",
    # "nabial",
    # "mieso",
    # "dania-gotowe",
    # "napoje",
    # "mrozone",
    # "artykuly-spozywcze",
    # "drogeria",
    # "dla-domu",
    # "dla-dzieci",
    # "dla-zwierzat",
]


URLS: list[str] = [f"{URL}{category}" for category in CATEGORIES]
