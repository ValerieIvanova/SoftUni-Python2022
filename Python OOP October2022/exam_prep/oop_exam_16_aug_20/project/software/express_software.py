from exam_prep.oop_exam_16_aug_20.project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name: str, capacity_consumption, memory_consumption):
        super().__init__(name, software_type='Express',
                         capacity_consumption=capacity_consumption,
                         memory_consumption=memory_consumption * 2)