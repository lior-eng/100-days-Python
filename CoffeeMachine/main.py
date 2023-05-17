import MENU

def check_resources(coffee: dict) -> bool:
    for item in coffee:
        if coffee[item] > MENU.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coins_inserted() -> float:
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transation_successful(money_received: float, drink_cost: float) -> bool:
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Your change is ${change:.2f}. ")
        MENU.profit += drink_cost
        return True
    else:
        print(f"Sorry, {money_received} that's not enough money for {choice}. Money refunded.")
        return False

def make_coffee(coffee: dict) -> None:
    for item in coffee:
        MENU.resources[item] -= coffee[item]

is_on = True

while is_on:
    choice = input("What would you like? espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
        print("Bye bye")
    elif choice == "report":
        print(f"Water: {MENU.resources['water']}ml")
        print(f"Milk: {MENU.resources['milk']}ml")
        print(f"Coffee: {MENU.resources['coffee']}g")
        print(f"Money: ${MENU.profit}")
    else:
        if check_resources(MENU.MENU[choice]["ingredients"]):
            payment = coins_inserted()
            if is_transation_successful(payment, MENU.MENU[choice]["cost"]):
                make_coffee(MENU.MENU[choice]["ingredients"])
                print(f"Here is your {choice}. Enjoy!.")
            else:
                is_on = False
        else:
            is_on = False

