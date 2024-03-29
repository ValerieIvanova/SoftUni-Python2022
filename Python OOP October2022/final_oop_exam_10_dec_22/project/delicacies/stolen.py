from final_oop_exam_10_dec_22.project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION = 250

    def __init__(self, name, price):
        super().__init__(name, Stolen.PORTION, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."