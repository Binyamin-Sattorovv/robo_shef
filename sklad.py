sklad = {
    "чай": 3,
    "сок": 3,
    "сэндвич": 3
}


def change_sklad(cart):
    
    for food in sklad:
        
        number = cart.count(food)

        if number > 0:
            sklad[food] = sklad[food] - number