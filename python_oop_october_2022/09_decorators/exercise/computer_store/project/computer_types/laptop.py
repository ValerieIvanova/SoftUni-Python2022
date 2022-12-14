from exam_prep.oop_exam_10_apr_22.project import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }
    MAX_RAM = 64

    def configure_computer(self, processor, ram):

        if processor not in Laptop.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram > Laptop.MAX_RAM or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
