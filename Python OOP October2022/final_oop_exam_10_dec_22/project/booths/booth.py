from abc import ABC, abstractmethod


class Booth(ABC):

    def __init__(self, booth_number, capacity):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []  # delicacies (objects) that are ordered.
        self.price_for_reservation = 0  # o	Each time a booth is reserved, the price for a reservation should be set.
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people):
        pass