from menu import show_menu, menu
from sklad import sklad, change_sklad
from cart import add_food, show_cart
from payment import pay
from cashier import show_help


def main():
    
    print("==============================")
    print("       КАФЕ РОБО-ШЕФ")
    print("==============================")

    cashier = input("Введите имя кассира: ").strip()

    while len(cashier) == 0:
        
        print("Имя не может быть пустым.")
        cashier = input("Введите имя кассира: ").strip()

    show_menu(sklad)

    clients = set()
    viruchka = 0
    orders = 0

    while orders < 3:
        
        print("\nВведите имя клиента.")
        print("Или напишите 'выход'.")

        name = input("> ").strip().lower()

        if name == "выход":
            
            break

        if len(name) == 0:
            
            print("Имя не может быть пустым.")
            continue

        if name in clients:
            
            print("Этот клиент уже обслужен.")
            continue

        cart = []

        print("\nКлиент:", name)
        print("Можно начинать заказ.")
        
        show_help()

        order_finished = False

        while not order_finished:
            command = input("\nКоманда: ").strip().lower()

            if command == "1":
                add_food(cart)

            elif command == "2":
                show_cart(cart)

            elif command == "3":
                show_help()

            elif command == "4":
                
                cart.clear()
                print("Заказ отменен.")
                order_finished = True

            elif command == "5":
                
                success, total = pay(cart)

                if success:
                    
                    change_sklad(cart)

                    viruchka = viruchka + total
                    orders = orders + 1
                    clients.add(name)

                    print("\nЗаказ клиента", name, "завершен.")
                    print("Текущая выручка:", viruchka, "сомони")

                    cart.clear()
                    order_finished = True

            elif command == "0":
                
                print("\nИгра закончена.")
                print("Выручка:", viruchka, "сомони")
                
                return

            else:
                
                print("Такой команды нет.")
                print("Напишите 'помощь'.")

        show_menu(sklad)

    print("\n==============================")
    print("       ИГРА ЗАКОНЧЕНА")
    print("==============================")
    print("Кассир:", cashier)
    print("Клиентов обслужено:", orders)
    print("Выручка:", viruchka, "сомони")

    print("\nОстатки:")

    for food in menu:
        
        print(food, "-", sklad[food])

    print("==============================")


if __name__ == "__main__":
    
    main()