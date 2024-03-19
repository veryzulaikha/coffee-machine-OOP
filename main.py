from money_conversion import MoneyMachine
from coffemaker import Maker, Report, ResourcesChecker
from menu import TheMenu

menu = TheMenu()
water = menu.resources["water"]
milk = menu.resources["milk"]
coffee = menu.resources["coffee"]
money = 0
end = False
while not end:
    request = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if request == "off":
        end = True
    elif request == "report":
        my_report = Report()
        my_report.report(water, milk, coffee, money)
    elif request != "espresso" and request != "latte" and request != "cappuccino":
        print("Invalid input")
    else:
        cost = menu.MENU[request]["cost"]
        water_needed = menu.MENU[request]["ingredients"]["water"]
        milk_needed = menu.MENU[request]["ingredients"]["milk"]
        coffee_needed = menu.MENU[request]["ingredients"]["coffee"]
        resources_checker = ResourcesChecker()
        sufficient = resources_checker.is_sufficient(water, milk, coffee, water_needed, milk_needed, coffee_needed)
        if sufficient is True:
            payment = MoneyMachine()
            change = payment.money_conversion(cost)
            my_coffee_maker = Maker()
            coffee_maker = my_coffee_maker.prepare_order(water, milk, coffee, water_needed, milk_needed, coffee_needed,
                                                         request, change)

            if coffee_maker is True:
                water -= water_needed
                milk -= milk_needed
                coffee -= coffee_needed
                money += cost
