from exam_prep.oop_exam_10_apr_22.project import DesktopComputer
from exam_prep.oop_exam_10_apr_22.project import Laptop


class ComputerStoreApp:
    VALID_TYPES = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse = []  # the built computers.
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):

        if type_computer == 'Desktop Computer':
            new_computer = DesktopComputer(manufacturer, model)
        elif type_computer == 'Laptop':
            new_computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        config = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)
        return config

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget \
                and computer.processor == wanted_processor \
                    and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."
        else:
            raise Exception("Sorry, we don't have a computer for you.")