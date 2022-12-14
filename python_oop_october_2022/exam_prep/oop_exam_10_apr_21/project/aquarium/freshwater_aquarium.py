from exam_prep.oop_exam_10_apr_21.project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 50

    def __init__(self, name):
        super().__init__(name, FreshwaterAquarium.INITIAL_CAPACITY)