from exam_prep.oop_exam_22_aug_20.project.appliances.fridge import Fridge
from exam_prep.oop_exam_22_aug_20.project.appliances.laptop import Laptop
from exam_prep.oop_exam_22_aug_20.project.appliances.tv import TV
from exam_prep.oop_exam_22_aug_20.project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * (len(children) + 2)
        self.calculate_expenses(self.appliances + self.children)
