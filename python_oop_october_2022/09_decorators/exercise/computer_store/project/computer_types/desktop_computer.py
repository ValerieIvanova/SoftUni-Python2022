from exam_prep.oop_exam_10_apr_22.project import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }
    MAX_RAM = 128

    def configure_computer(self, processor, ram):
        if processor not in DesktopComputer.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram > DesktopComputer.MAX_RAM or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
