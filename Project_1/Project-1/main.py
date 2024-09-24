from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

menu = Menu()
coffe_maker = CoffeeMaker()
money = MoneyMachine()

list_items = menu.get_items()


while is_on:
    choice = input(f"What would you like? {list_items}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money.report()
        coffe_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)