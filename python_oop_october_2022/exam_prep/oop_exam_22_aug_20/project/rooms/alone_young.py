from exam_prep.oop_exam_22_aug_20.project.appliances.tv import TV
from exam_prep.oop_exam_22_aug_20.project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name, salary):
        super().__init__(family_name, budget=salary, members_count=1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)

