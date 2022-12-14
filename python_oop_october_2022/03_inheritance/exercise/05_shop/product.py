class Product:
    def __init__(self, name, quantity):
        self.quantity = quantity
        self.name = name

    def decrease(self, quantity):
        if self.quantity - quantity >= 0:
            self.quantity -= quantity

    def increase(self, quantity):
        self.quantity += quantity

    def __repr__(self):
        return self.name