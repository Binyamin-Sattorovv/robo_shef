from menu import menu, price
from sklad import sklad


def get_total(cart):
    
    total = 0

    for food in cart:
        total = total + price[food]

    return total


def show_cart(cart):
    
    if len(cart) == 0:
        print("Корзина пустая.")
        return

    print("\n--- ВАШ ЗАКАЗ ---")

    for food in menu:
        
        number = cart.count(food)

        if number > 0:
            cost = price[food] * number

            print(
                food,
                "x",
                number,
                "=",
                cost,
                "сомони"
            )

    print("Всего:", get_total(cart), "сомони")


def add_food(cart):
    
    food = input("Какое блюдо добавить? ").strip().lower()

    if food not in menu:
        
        print("Такого блюда нет.")
        return

    try:
        
        number = int(input("Сколько порций? ").strip())
        
    except ValueError:
        
        print("Нужно ввести число.")
        
        return

    if number <= 0:
        
        print("Количество должно быть больше 0.")
        
        return

    if number > 3:
        
        print("За один раз можно добавить максимум 3 порции.")
        
        return

    already = cart.count(food)
    can_add = sklad[food] - already

    if number > can_add:
        
        print("Недостаточно блюда на складе.")
        print("Можно добавить:", max(0, can_add))
        
        return

    for i in range(number):
        
        cart.append(food)

    print("Блюдо добавлено.")
    
    show_cart(cart)