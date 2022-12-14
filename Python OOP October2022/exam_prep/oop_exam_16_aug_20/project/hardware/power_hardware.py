from math import floor

from exam_prep.oop_exam_16_aug_20.project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name: str, capacity, memory):
        super().__init__(name, hardware_type='Power',
                         capacity=floor(capacity * 0.25),
                         memory=floor(memory + (memory * 0.75)))