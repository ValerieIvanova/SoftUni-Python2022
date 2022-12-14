from exam_prep.oop_exam_10_apr_21.project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    COMFORT = 5
    PRICE = 10

    def __init__(self):
        super().__init__(Plant.COMFORT, Plant.PRICE)