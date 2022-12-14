class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []  # all meals (objects) added by the client
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value.startswith('0') and\
                len(value) == 10 and\
                value.isdigit():
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")