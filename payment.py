from menu import menu, price
from cart import get_total


def pay(cart):

    if len(cart) == 0:
        
        print("Сначала добавьте блюдо.")
        
        return False, 0

    total = get_total(cart)

    print("Сумма заказа:", total, "сомони")

    try:
        
        money = int(input("Введите деньги: ").strip())

    except ValueError:
        
        print("Введите целое число.")
        return False, 0

    if money <= 0:
        
        print("Сумма должна быть больше 0.")
        return False, 0

    if money < total:
        
        print("Денег недостаточно.")
        print("Не хватает:", total - money, "сомони")
        
        return False, 0

    change = money - total

    print("\nОплата прошла успешно.")
    print("Сдача:", change, "сомони")

    print("\n--- ЧЕК ---")

    for food in menu:
        
        number = cart.count(food)

        if number > 0:
            print(
                food,
                "x",
                number,
                "=",
                price[food] * number,
                "сомони"
            )

    return True, total