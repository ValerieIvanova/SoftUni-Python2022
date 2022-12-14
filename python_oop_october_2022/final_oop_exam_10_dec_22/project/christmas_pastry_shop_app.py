from final_oop_exam_10_dec_22.project.booths.open_booth import OpenBooth
from final_oop_exam_10_dec_22.project.booths.private_booth import PrivateBooth
from final_oop_exam_10_dec_22.project.delicacies.gingerbread import Gingerbread
from final_oop_exam_10_dec_22.project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES_REF = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen,
    }

    BOOTH_TYPES_REF = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth,
    }

    def __init__(self):
        self.booths = []  # all booths (objects) that are created.
        self.delicacies = []  # all delicacies (objects) that are created.
        self.income = 0.0  # the total income of the pastry shop.

    def __find_booth(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth

    def __find_delicacy(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy

    def add_delicacy(self, type_delicacy, name, price):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in ChristmasPastryShopApp.DELICACY_TYPES_REF:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = ChristmasPastryShopApp.DELICACY_TYPES_REF[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in ChristmasPastryShopApp.BOOTH_TYPES_REF:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = ChristmasPastryShopApp.BOOTH_TYPES_REF[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        for booth in self.booths:
            if not booth.is_reserved and number_of_people <= booth.capacity:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth(booth_number)
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        output = [f"Booth {booth.booth_number}:",
                  f"Bill: {bill:.2f}lv."]
        return '\n'.join(output)

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

#
# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
