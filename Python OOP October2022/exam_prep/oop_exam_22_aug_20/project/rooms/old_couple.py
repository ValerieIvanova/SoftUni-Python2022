from exam_prep.oop_exam_22_aug_20.project.appliances.fridge import Fridge
from exam_prep.oop_exam_22_aug_20.project.appliances.stove import Stove
from exam_prep.oop_exam_22_aug_20.project.appliances.tv import TV
from exam_prep.oop_exam_22_aug_20.project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, budget=pension_one+pension_two, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)
