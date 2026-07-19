from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
available = CoffeeMaker()
money = MoneyMachine()

print(menu.get_items())
available.report()          

order = input("Enter the item: ")

drink = menu.find_drink(order)

if drink:

    if available.is_resource_sufficient(drink):

        if money.make_payment(drink.cost):

            available.make_coffee(drink)

available.report()
money.report()