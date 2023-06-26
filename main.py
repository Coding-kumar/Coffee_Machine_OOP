from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_menu=Menu()
coffe_make=CoffeeMaker()
coffe_money=MoneyMachine()

order_name=input(f"select the menu {coffe_menu.get_items()}").lower()
item=coffe_menu.find_drink(order_name)

if item.name == order_name:
    avail=coffe_make.is_resource_sufficient(item)
    if avail==True:
        payment=coffe_money.make_payment(item.cost)
        if payment==True:
            coffe_make.make_coffee(item)
            coffe_make.report()
            coffe_money.report()
        else:
            print("Payment failed")
    else:
        print("resources not enough to prepare coffee")

else:
    print("item not available")





