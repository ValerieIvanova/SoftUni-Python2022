class Room:

    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []  # all kids in that room (objects)
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total = 0
        for elements in args:
            for el in elements:
                if type(el).__name__ == 'Child':
                    total += el.cost * 30
                else:
                    total += el.get_monthly_expense()

        self.expenses = total
