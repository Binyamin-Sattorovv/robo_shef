menu = ("чай", "сок", "сэндвич")

price = {
    "чай": 10,
    "сок": 15,
    "сэндвич": 25
}


def show_menu(sklad):
    
    print("\n--- МЕНЮ ---")

    for food in menu:
        print(
            food,
            "-",
            price[food],
            "сомони",
            "| осталось:",
            sklad[food]
        )