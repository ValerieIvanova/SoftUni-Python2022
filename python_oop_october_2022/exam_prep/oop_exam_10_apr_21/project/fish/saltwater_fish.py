from exam_prep.oop_exam_10_apr_21.project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INITIAL_SIZE = 5
    SIZE_INCREASE = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, SaltwaterFish.INITIAL_SIZE, price)

