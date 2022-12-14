from exam_prep.oop_exam_10_apr_21.project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INITIAL_SIZE = 3
    SIZE_INCREASE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, FreshwaterFish.INITIAL_SIZE, price)