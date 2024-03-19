class MoneyMachine:

    @staticmethod
    def money_conversion(cost):
        print("Please insert coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels?"))
        pennies = int(input("How many pennies?"))
        total_amount = float(((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1)) / 100)
        change = round((total_amount - cost), 2)
        return change
