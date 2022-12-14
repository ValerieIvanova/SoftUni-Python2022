from exam_prep.oop_exam_10_apr_22.project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name, energy=15):
        super().__init__(name, energy)

