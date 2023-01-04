class Property():
    '''
    Property class to be used with property_calculator function
    '''

    def __init__(self, price, rent):
        self.price = price
        self.rent = rent
        self.investment = 0
        self.monthly_expenses = 0
        self.annual_cashflow = 0
        self.roi = 0

    def calc_investment(self):
        validate_input = True
        while validate_input:
            money_down = input("\nHow much are you willing to invest up front to own this property? Enter a whole number (no decimal point) if you know the exact amount, or a whole number followed by the percent sign '%' if you will invest a percentage of the total price: ")
            if "%" in money_down:
                try:
                    money_down = (int(money_down.strip("%")))/100
                except ValueError:
                    print("\nWow! You can't even follow simple instructions, can you?")
                else:
                    self.investment = self.price * money_down
                    validate_input = False
            else:
                try:
                    money_down = int(money_down)
                except ValueError:
                    print("\nWow! You can't even follow simple instructions, can you?")
                else:
                    self.investment = money_down
                    validate_input = False

    def calc_expenses(self):
        validate_input = True
        while validate_input:
            monthly_expenses = input(
                "\nHow much will it cost you each month to maintain this property? Don't forget to include your mortgage, money you set aside for repairs and any other monthly expenses you might incur as a landlord. Please enter a whole number: ")
            try:
                monthly_expenses = int(monthly_expenses)
            except ValueError:
                print("\nWow! You can't even follow simple instructions, can you?")
            else:
                self.monthly_expenses = monthly_expenses
                validate_input = False

    def calc_cashflow_and_roi(self):
        monthly_cashflow = self.rent - self.monthly_expenses
        self.annual_cashflow = monthly_cashflow * 12
        try:
            self.roi = (self.annual_cashflow/self.investment) * 100
        except ZeroDivisionError:
            self.roi = "undefined"


def property_calculator():
    '''
        property_calculator function to be used with Property class
        a little bit sassy
        never explicitly mentions the proletariat or the bourgeoisie, still might be a communist
    '''
    print("So you want to be a slumlord and can't do math! Well, that adds up. But don't worry! I am here to help you! In order to do so, I will need some information about the property you are interested in.")
    validate_input = True
    while validate_input:
        price = input(
            "\nPlease enter the price of the property you are thinking about buying, as a whole number(no commas or decimal points, please): ")
        try:
            price = int(price)
        except ValueError:
            print("\nWow! You can't even follow simple instructions, can you?")
        else:
            validate_input = False
    validate_input = True
    while validate_input:
        rent = input(
            "\nPlease enter the amount you hope to extract from your peasants each month, as a whole number: ")
        try:
            rent = int(rent)
        except ValueError:
            print("\nWow! You can't even follow simple instructions, can you?")
        else:
            validate_input = False
    property = Property(price, rent)
    property.calc_investment()
    property.calc_expenses()
    property.calc_cashflow_and_roi()
    print(f"\nWith a down payment of ${property.investment} on a property that costs ${property.price}, rented at ${property.rent} per month, with a mortgage and other monthly expenses totalling ${property.monthly_expenses} per month, you will make ${property.annual_cashflow} each year, reflecting a cash-on-cash return on investment of {property.roi}%.")


property_calculator()
