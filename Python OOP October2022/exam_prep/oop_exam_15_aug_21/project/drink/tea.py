from exam_prep.oop_exam_15_aug_21.project.drink.drink import Drink


class Tea(Drink):
    PRICE = 2.5

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, Tea.PRICE, brand)
