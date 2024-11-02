def add_potion(shop: dict, name: str, price: str):
    shop[name] = price


def remove_potion(shop: dict, name):
    del shop[name]


def update_price(shop: dict, name: str, new_price: str):
    shop[name] = new_price


def display_shop(shop: dict):
    for key in shop:
        print(f"{key}: {shop[key]}")


potions_shop = {"Зілля здоров'я": 250,
                "Драконячий тонік": 150,
                "Зілля від кашлю": 50,
                "Крововідновлювальне зілля": 120
                }


while True:
    action = input("Choice action: 1)Display shop; 2)Add new potion; 3)Update price; 4)Remove potion; 5)Exit \n Your choice is  ")
    if action.lower() == "display shop" or action.lower() == "1":
        display_shop(potions_shop)
    elif action.lower() == "add new potion" or action.lower() == "2":
        potion_name = input("Please, enter potion name: ")
        price = input("Please, enter potion price: ")
        add_potion(potions_shop, potion_name, price)
    elif action.lower() == "update price" or action.lower() == "3":
        potion_name = input("Please, enter potion name which price you want to update: ")
        new_price = input("Please, enter new price: ")
        update_price(potions_shop, potion_name, new_price)
    elif action.lower() == "update price" or action.lower() == "4":
        potion_name = input("Please, enter potion name which price you want to update: ")
        remove_potion(potions_shop, potion_name)
    elif action.lower() == "exit" or action.lower() == "5":
        break
    else:
        print("Incorrect choice! Try again")
