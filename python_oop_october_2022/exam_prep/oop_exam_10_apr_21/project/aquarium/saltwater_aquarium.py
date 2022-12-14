from exam_prep.oop_exam_10_apr_21.project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 25

    def __init__(self, name):
        super().__init__(name, SaltwaterAquarium.INITIAL_CAPACITY)
