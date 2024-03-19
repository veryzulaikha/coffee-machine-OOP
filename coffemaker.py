class Maker:

    @staticmethod
    def prepare_order(water, milk, coffee, water_needed, milk_needed, coffee_needed, request, change):

        if water >= water_needed and milk >= milk_needed and coffee >= coffee_needed:
            if change == 0:
                print(f"Here is your {request} ☕. Enjoy!")
                return True
            elif change > 0:
                print(f"Here is ${change} in change.")
                print(f"Here is your {request} ☕. Enjoy!")
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
                return False


class Report:

    @staticmethod
    def report(water, milk, coffee, money):
        print(f"water: {water}ml")
        print(f"milk: {milk}ml")
        print(f"coffee: {coffee}ml")
        print(f"money: ${money}")


class ResourcesChecker:
    @staticmethod
    def is_sufficient(water, milk, coffee, water_needed, milk_needed, coffee_needed):
        if water < water_needed and milk < milk_needed:
            print("Sorry there is not enough milk and water.")
            return False
        elif water < water_needed and coffee < coffee_needed:
            print("Sorry there is not enough coffee and water.")
            return False
        elif milk < milk_needed and coffee < coffee_needed:
            print("Sorry there is not enough coffee and milk.")
            return False
        elif water < water_needed:
            print("Sorry there is not enough water.")
            return False
        elif milk < milk_needed:
            print("Sorry there is not enough milk.")
            return False
        elif coffee < coffee_needed:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
