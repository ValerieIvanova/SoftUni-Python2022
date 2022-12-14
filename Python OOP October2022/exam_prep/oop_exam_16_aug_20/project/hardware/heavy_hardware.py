from math import floor

from exam_prep.oop_exam_16_aug_20.project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name: str, capacity, memory):
        super().__init__(name, hardware_type='Heavy',
                         capacity=capacity * 2,
                         memory=floor(memory * 0.75))