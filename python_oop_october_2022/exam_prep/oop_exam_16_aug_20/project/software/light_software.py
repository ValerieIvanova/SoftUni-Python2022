from math import floor

from exam_prep.oop_exam_16_aug_20.project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption, memory_consumption):
        super().__init__(name, software_type='Light',
                         capacity_consumption=floor(capacity_consumption + capacity_consumption * 0.5),
                         memory_consumption=floor(memory_consumption * 0.5))
