class Appliance:
    def __init__(self, cost):
        self.cost = cost  # The cost is for a single day

    def get_monthly_expense(self):
        return 30 * self.cost