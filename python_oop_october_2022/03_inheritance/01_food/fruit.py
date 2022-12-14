from food import Food


class Fruit(Food):

    def __init__(self, name: str, expiration_date):
        super().__init__(expiration_date)
        self.name = name